# Mapa da arquitetura original

## Evidência disponível

```text
ZIP oficial para UN40J5200AGXZD, versão 1080.0
└── T-N14MJUABC/
    ├── info.txt                 "T-N14MJUABC 1080.0"
    └── image/upgrade.msd        contêiner MSDU10, 661.309.282 bytes
        ├── cabeçalho e tabela observada de 13 regiões
        ├── 13 regiões contíguas de dados opacos
        └── 4 bytes finais não interpretados
```

Os deslocamentos, comprimentos, SHA-256 e amostras estão em `analysis/inventory.json`. A tabela foi interpretada somente como triplas de inteiros little endian (`id bruto`, `offset`, `comprimento`) porque todas as regiões ficam nos limites do arquivo e se encadeiam; o significado dos IDs é desconhecido. O marcador `Salted__` aparece no cabeçalho no deslocamento decimal 198 **e em cada uma das 13 regiões, sempre 136 bytes após o início**. Isso é forte evidência de envelopes cifrados com sal, mas não demonstra algoritmo, chave, modo, assinatura ou conteúdo dos blocos.

## Plataforma de aplicativos

A [tabela oficial de grupos](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) classifica `UJ5200` no grupo `15TV_ENTRY`, **Samsung Legacy Platform**, `TV SDK 5.1`. O prefixo `U` da tabela não é uma identificação direta de CPU ou sistema operacional; a associação do modelo brasileiro deve ser confirmada na própria TV ou pelo SDK.

O hardware `DB04` foi informado pelo proprietário; não aparece nos metadados externos do ZIP. A correspondência exata entre essa revisão de hardware e os blocos do MSD não pôde ser verificada offline.

## Camadas ainda não identificadas

| Camada | Estado |
| --- | --- |
| CPU, endianness da CPU, RAM | Desconhecidos. Little endian da tabela MSD não implica endianness da CPU. |
| Bootloader, kernel, sistema operacional base | Desconhecidos; não há executáveis legíveis expostos. |
| Partições, sistemas de arquivos, bibliotecas | Desconhecidos; nenhuma imagem de partição foi extraída. |
| Processos, serviços, Smart Hub nativo, gerenciador de memória | Desconhecidos; dependem de firmware decifrado ou medições na TV. |
| USB firmware | Estrutura externa observada e [fluxo oficial de atualização](https://www.samsung.com/br/support/tv-audio-video/how-to-update-the-samsung-tvs-firmware-using-a-usb-drive/) documentado. Validação criptográfica interna não foi caracterizada. |
| USB aplicativos | [Teste legado com `.sig` oficial](https://developer.samsung.com/smarttv/legacy/samsung-legacy-platform-faq.html) documentado; suporte exato desta unidade ainda precisa ser verificado. |

O mapa não afirma Linux, Android ou Tizen para o firmware nativo. A classificação “Legacy Platform” descreve o ambiente de aplicativo, não prova a implementação do kernel.
