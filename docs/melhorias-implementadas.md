# Melhorias implementadas

`src/prototype/` contém um protótipo web local com cinco opções visuais, foco visível, navegação por setas e Escape, sem bibliotecas externas ou animações. Ele demonstra uma forma de reduzir passos na navegação. Os botões só atualizam texto de estado; não invocam APIs da Samsung, não trocam entrada HDMI e não iniciam aplicativos. `build.sh` gera uma cópia em `build/NAO_INSTALAVEL/`.

`src/analyze_firmware.py` automatiza inventário, hashes, CRC do ZIP, comparação com a pasta descompactada e validação de limites da tabela MSD. `tests/test_analyze_firmware.py` cobre regiões contíguas, sobreposição e comprimento fora do arquivo. Essas melhorias dizem respeito ao processo de análise e a um conceito de UI. Não alteram desempenho do firmware original.

`tests/test_prototype.js` verifica navegação por setas em telas largas e estreitas, limite da lista, seleção e Escape. Dois builds consecutivos têm hashes iguais dos três arquivos de saída. Não houve benchmark de CPU/RAM na TV.

Uma aplicação real exigiria projeto do Samsung TV SDK 5.1, teste em emulador compatível e confirmação das APIs e do formato de pacote. Nenhum desses recursos foi inventado ou presumido aqui.
