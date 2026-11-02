# Riscos e recuperação

Nenhum bootloader, partição, serviço ou firmware foi alterado. O risco local é apenas consumo de disco e tempo de leitura do arquivo de 631 MiB. O maior risco futuro seria tentar instalar um pacote sem suporte, interromper uma atualização ou confundir o protótipo com firmware. Não faça isso.

Para uma atualização **oficial** futura, a [Samsung orienta usar apenas o download do modelo correto](https://www.samsung.com/br/support/tv-audio-video/how-to-update-the-samsung-tvs-firmware-using-a-usb-drive/) e não desligar a TV nem remover USB durante o processo. Se o pacote não for reconhecido, conferir modelo, extração e posicionamento dos arquivos; persistindo, contatar o suporte Samsung. Não foi encontrado procedimento oficial de recuperação por imagem de partição, e este projeto não propõe um.

As verificações internas de integridade e assinatura do firmware `upgrade.msd` não foram caracterizadas. O marcador `Salted__` não prova assinatura digital nem segurança de boot. Não se deve alegar que um pacote reempacotado passaria na TV.
