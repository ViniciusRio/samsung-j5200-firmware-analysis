# Samsung UN40J5200AGXZD: análise local

Este repositório inventaria o pacote USB oficial `T-N14MJUABC` versão 1080.0 e contém um protótipo de interface **NÃO INSTALÁVEL**. Nenhum arquivo do firmware original é alterado ou executado.

## Reprodução

Requer Python 3.10+ e Node.js para os testes da interface; não precisa de bibliotecas externas para a análise básica.

O firmware original e as cópias binárias de análise não são redistribuídos neste repositório público. Baixe `T-N14MJUABC.zip` versão 1080.0 na [página oficial da Samsung para UN40J5200AGXZD](https://www.samsung.com/br/support/model/UN40J5200AGXZD/), coloque o ZIP na raiz do projeto e descompacte-o ali, formando `T-N14MJUABC/info.txt` e `T-N14MJUABC/image/upgrade.msd`. Confira os hashes publicados em `original/SHA256SUMS` antes de tirar conclusões baseadas na mesma amostra.

```sh
sh build.sh
```

O comando testa o parser, compara o ZIP com a pasta descompactada, verifica CRC e SHA-256, grava `analysis/inventory.json` e copia o protótipo para `build/NAO_INSTALAVEL/`. Abra `build/NAO_INSTALAVEL/index.html` num navegador para testar a navegação; isso **não** é um aplicativo Samsung nem uma atualização.

As verificações registradas ficam em `analysis/test-run.log`, `analysis/original-integrity.txt` e `analysis/build-hashes-*.txt`. Não há medição de desempenho da televisão.

Os resultados estáticos já obtidos estão em `analysis/`. As dependências instaladas localmente, logs de instalação e caminhos específicos da configuração MCP não fazem parte do repositório; o procedimento e as versões estão documentados em `docs/engenharia-reversa.md`.

`build/NAO_INSTALAVEL/` também contém a cópia experimental produzida neste trabalho. `release/` permanece vazio. O pacote de firmware Samsung não é recompilado.

## Resultados principais

- O ZIP contém `info.txt` e `image/upgrade.msd`; os arquivos extraídos coincidem com os membros do ZIP.
- O `upgrade.msd` tem marcador `MSDU10`, uma tabela observada de 13 regiões, marcador `Salted__` no cabeçalho e payloads sem formatos de arquivo identificáveis no início. Não foi possível identificar CPU, kernel, partições, serviços ou aplicação nativa a partir desse pacote.
- A varredura completa com Binwalk e a amostra de 64 MiB inspecionada pelo REA não estabeleceram imagens de partição ou binários utilizáveis; veja `docs/engenharia-reversa.md` para os limites de tamanho e falsos positivos.
- O grupo J5200 de 2015 consta na [lista oficial da Samsung](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) como **Samsung Legacy Platform**, com TV SDK 5.1. O arquivo e a versão também constam na [página do modelo](https://www.samsung.com/br/support/model/UN40J5200AGXZD/).
- A [FAQ da plataforma legada](https://developer.samsung.com/smarttv/legacy/samsung-legacy-platform-faq.html) descreve teste de aplicativo por USB com assinatura `.sig` fornecida pela Samsung para o DUID da TV. Sem essa assinatura e sem validação no dispositivo, não há pacote instalável entregue.

Veja `docs/` para evidências, limitações, instalação e riscos.
