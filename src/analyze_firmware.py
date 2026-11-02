#!/usr/bin/env python3
"""Read-only inventory of the supplied Samsung USB update container.

The MSD entry meanings are deliberately left unnamed: only their observed
layout and bounds are reported. No payload is decrypted or executed.
"""
import argparse
import hashlib
import json
import math
import struct
import zipfile
from pathlib import Path


MAGICS = {"ELF": b"\x7fELF", "SquashFS_le": b"hsqs", "SquashFS_be": b"sqsh",
          "UBI": b"UBI#", "ZIP": b"PK\x03\x04", "OpenSSL_salted": b"Salted__"}


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def entropy(data):
    if not data:
        return 0.0
    return -sum((count / len(data)) * math.log2(count / len(data))
                for count in (data.count(i) for i in range(256)) if count)


def inspect_msd(path):
    size = path.stat().st_size
    with path.open("rb") as stream:
        header = stream.read(4096)
        if header[:6] != b"MSDU10":
            raise ValueError("assinatura MSDU10 ausente")
        if len(header) < 10:
            raise ValueError("cabecalho truncado")
        count = struct.unpack_from("<I", header, 6)[0]
        if not 0 < count <= 128 or len(header) < 10 + count * 12:
            raise ValueError("tabela de regioes invalida")
        entries = []
        previous_end = 0
        for index in range(count):
            ident, offset, length = struct.unpack_from("<III", header, 10 + index * 12)
            end = offset + length
            if offset < 10 + count * 12 or offset < previous_end or end > size:
                raise ValueError(f"regiao {index + 1} fora dos limites ou sobreposta")
            stream.seek(offset)
            sample = stream.read(min(length, 65536))
            entries.append({"index": index + 1, "raw_id": ident, "offset": offset,
                            "length": length, "end": end,
                            "first_16_hex": sample[:16].hex(),
                            "salted_marker_relative_offset": sample.find(b"Salted__"),
                            "sample_entropy_bits_per_byte": round(entropy(sample), 4),
                            "sample_magic_at_start": [name for name, magic in MAGICS.items()
                                                      if sample.startswith(magic)]})
            previous_end = end
    return {"magic": "MSDU10", "size": size, "entry_count": count,
            "table_end": 10 + count * 12,
            "header_salted_marker_offset": header.find(b"Salted__"),
            "trailing_bytes": size - previous_end, "entries": entries}


def inspect_zip(path):
    with zipfile.ZipFile(path) as archive:
        members = []
        for item in archive.infolist():
            if item.filename.startswith("/") or ".." in Path(item.filename).parts:
                raise ValueError("caminho ZIP inseguro")
            members.append({"name": item.filename, "size": item.file_size,
                            "compressed_size": item.compress_size,
                            "crc32": f"{item.CRC:08x}"})
        bad = archive.testzip()
        if bad:
            raise ValueError(f"CRC invalido: {bad}")
    return members


def analyze(root):
    zip_path = root / "T-N14MJUABC.zip"
    msd_path = root / "T-N14MJUABC/image/upgrade.msd"
    info_path = root / "T-N14MJUABC/info.txt"
    paths = [zip_path, msd_path, info_path]
    if any(not path.is_file() for path in paths):
        raise FileNotFoundError("ZIP, upgrade.msd ou info.txt ausente")
    report = {"files": {str(path.relative_to(root)): {"size": path.stat().st_size,
              "sha256": digest(path)} for path in paths}, "zip_members": inspect_zip(zip_path),
              "info_text": info_path.read_text(encoding="ascii").strip(),
              "msd": inspect_msd(msd_path)}
    with zipfile.ZipFile(zip_path) as archive:
        for rel in ("T-N14MJUABC/info.txt", "T-N14MJUABC/image/upgrade.msd"):
            target = root / rel
            h = hashlib.sha256()
            with archive.open(rel) as source:
                for chunk in iter(lambda: source.read(1024 * 1024), b""):
                    h.update(chunk)
            report.setdefault("zip_matches_extracted", {})[rel] = h.hexdigest() == digest(target)
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = analyze(args.root)
    content = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
