import struct
import tempfile
import unittest
from pathlib import Path

from src.analyze_firmware import inspect_msd


class MsdLayoutTests(unittest.TestCase):
    def make_file(self, entries, total=128):
        temp = tempfile.TemporaryDirectory()
        path = Path(temp.name) / "sample.msd"
        data = bytearray(total)
        data[:6] = b"MSDU10"
        struct.pack_into("<I", data, 6, len(entries))
        for index, entry in enumerate(entries):
            struct.pack_into("<III", data, 10 + index * 12, *entry)
        path.write_bytes(data)
        self.addCleanup(temp.cleanup)
        return path

    def test_valid_contiguous_regions(self):
        result = inspect_msd(self.make_file([(1, 40, 20), (2, 60, 68)]))
        self.assertEqual(result["entry_count"], 2)
        self.assertEqual(result["trailing_bytes"], 0)

    def test_rejects_overlapping_regions(self):
        with self.assertRaises(ValueError):
            inspect_msd(self.make_file([(1, 40, 30), (2, 60, 20)]))

    def test_rejects_out_of_bounds(self):
        with self.assertRaises(ValueError):
            inspect_msd(self.make_file([(1, 40, 100)]))


if __name__ == "__main__":
    unittest.main()
