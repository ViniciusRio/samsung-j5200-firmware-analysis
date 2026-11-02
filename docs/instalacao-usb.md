# USB: firmware e aplicativos

## Firmware oficial

A [Samsung lista `T-N14MJUABC.zip` 1080.0 para UN40J5200AGXZD](https://www.samsung.com/br/support/model/UN40J5200AGXZD/) e [orienta descompactar o download no nível principal do USB](https://www.samsung.com/br/support/tv-audio-video/how-to-update-the-samsung-tvs-firmware-using-a-usb-drive/). Este repositório não recomenda instalar o firmware: a versão já presente na TV e a integridade do download frente à origem Samsung não foram confirmadas. Nenhum arquivo aqui é uma atualização modificada.

## Aplicativos legados

A [FAQ oficial da Samsung](https://developer.samsung.com/smarttv/legacy/samsung-legacy-platform-faq.html) identifica o pacote de aplicativo legado como ZIP produzido pelo TV SDK legado e descreve teste por USB mediante assinatura `.sig` fornecida pelo Samsung Apps TV Seller Office para o DUID da TV; pacote e assinatura ficam na raiz do USB. Ela também cita conta `develop` e `CPDeveloper.sig` ou `Developer.sig` em alguns modelos. Isso é um procedimento condicionado à Samsung e ao aparelho, não uma licença para criar assinatura própria. A documentação geral de Tizen que nega instalação `.wgt` via USB não se aplica automaticamente à plataforma legada da J5200.

O SDK 5.1, DUID, assinatura oficial e teste no aparelho não estão disponíveis neste projeto. Por isso `release/` está vazio e `build/NAO_INSTALAVEL/` **não** deve ser copiado ao USB como aplicativo. Não há pacote validado para esta TV.

## Próximo teste não destrutivo, se autorizado depois

Confirmar na tela da TV o código do modelo, versão atual e se o menu de desenvolvimento legado existe. Não iniciar atualização, instalação ou redefinição para essa verificação. Para pacote de aplicativo, primeiro obter assinatura e instruções atuais no canal oficial da Samsung; só então validar o pacote com o SDK e testar voluntariamente na TV.
