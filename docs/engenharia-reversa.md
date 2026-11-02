# Engenharia reversa: procedimentos e evidências

## Entrada e integridade

Arquivos originais preservados no diretório raiz. Os hashes estão em `original/SHA256SUMS` e `analysis/inventory.json`. `unzip -t` passou; os dois arquivos extraídos são idênticos aos membros ZIP correspondentes. `info.txt` contém `T-N14MJUABC 1080.0`. A [página Samsung do modelo](https://www.samsung.com/br/support/model/UN40J5200AGXZD/) lista `T-N14MJUABC.zip` 1080.0 como atualização USB.

## MSD

`file` informa apenas `data`. Os 6 primeiros bytes são `MSDU10`. Bytes 6–9, lidos como inteiro little endian, dão 13. A partir do byte 10 há 13 triplas de inteiros little endian; a primeira região começa em 2006 e a última termina 4 bytes antes do fim. Amostras de 64 KiB de regiões maiores têm entropia próxima de 8 bits/byte; isso não prova criptografia, já que compressão também produz alta entropia. Nenhuma amostra começa com ELF, SquashFS, UBI ou ZIP. O marcador `Salted__` está no byte 198 do cabeçalho e 136 bytes após o início de **cada** região. `readelf` rejeita o MSD como não ELF. Não foram decifrados nem executados dados proprietários.

## REA e ferramentas

O [README do REA](https://github.com/morluto/rea) e o [guia de firmware](https://github.com/morluto/rea/blob/main/docs/firmware-analysis.md) foram consultados. REA 6.8.0 e Node 24.22.1 foram instalados localmente em `tools/rea-runtime/`; o Node inicial era 24.21.0. O MCP foi registrado em `~/.codex/config.toml` apontando explicitamente para o Node novo e requer reinício do Codex para aparecer nesta sessão. A CLI do REA foi executada: `inspect-artifact` rejeitou `upgrade.msd` como `unsupported binary format` (`analysis/rea-artifact.json`). Essa rejeição é esperada porque o MSD não é um ELF ou formato de aplicativo suportado pela operação genérica. Binwalk 3.1.x e Unblob 26.6.x são fornecidos separadamente e o REA usa `ps` e `prlimit` no Linux. `ps` e `prlimit` estão presentes. Ghidra não foi encontrado; de todo modo, não há ELF extraído para carregar. A análise básica foi feita com Python, `file`, `xxd`, `unzip` e hashes.

Unblob 26.6.4 foi instalado localmente e executado em modo `--skip-extraction`, sem copiar payloads. `analysis/unblob-report.json` detectou um trecho `lz4_skippable` em 73.208.522–161.551.527. O cabeçalho desse candidato está dentro de uma região que também tem `Salted__` e alta entropia; como o magic LZ4 skippable tem poucos bits fixos, pode ser um falso positivo em dados cifrados. **Não** foi tratado como sistema de arquivos, componente ou região de firmware validada. Não foi extraído nem executado.

Binwalk 3.1.0 foi compilado a partir da [versão oficial](https://github.com/ReFirmLabs/binwalk/releases/tag/v3.1.0) dentro de Docker e executado em contêiner sem rede e com o diretório do projeto montado somente para leitura. `analysis/binwalk-full.txt` cobre o MSD completo: a busca ampla produziu muitas assinaturas curtas de zlib e GPG em dados de alta entropia, sem evidência estrutural de sistemas de arquivos, ELF ou partições. A palavra `GPG` no relatório é uma **correspondência de assinatura**, não prova de assinatura digital válida. Binwalk reconheceu alguns dos marcadores `Salted__` que o parser encontrou em todas as 13 regiões.

`inspect-firmware-regions` do REA recusou o MSD inteiro porque a versão 6.8.0 limita entradas a 128 MiB (`analysis/rea-firmware.json`). Uma cópia somente de leitura dos primeiros 64 MiB foi criada em `extracted/msd-primeiros-64MiB.bin` e analisada com REA + Binwalk; o Evidence está em `analysis/rea-firmware-sample.json`. O REA registrou 88 candidatos na amostra, inclusive dois `openssl` nos deslocamentos 198 e 2142. A maioria dos demais candidatos é curta e não foi validada como arquivo real. A amostra não representa cobertura REA dos 631 MiB; a varredura completa foi feita diretamente por Binwalk.

## Limites

Sem payload acessível e sem coleta na TV, não é possível identificar com rigor CPU, kernel, partições, processo de boot, serviços, bibliotecas, UI nativa, dependências entre componentes, política de memória ou regras internas de assinatura. Nomes de regiões numéricas não são nomes de partições.
