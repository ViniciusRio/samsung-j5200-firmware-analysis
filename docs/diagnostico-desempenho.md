# Diagnóstico de desempenho

Não há medições da televisão, logs de boot, lista de processos, uso de RAM, perfil de CPU, tempos de abertura ou contagem de quadros. A queixa de lentidão é observação do usuário; as causas específicas permanecem hipóteses.

| Sintoma | Hipóteses para medir na TV | Medição segura proposta |
| --- | --- | --- |
| Ligar | Inicialização, rede ou armazenamento | Cronometrar energia até imagem e até controle responder, 5 repetições. |
| Smart Hub | Carregamento de recursos ou rede | Cronometrar tecla Smart Hub até primeiro quadro utilizável, com e sem rede. |
| Controle remoto | Fila de UI ou pilhas | Filmar tecla e reação em 60 fps, sem menus de serviço. |
| Travamentos | Pressão de memória ou E/S | Registrar app, sequência, duração e necessidade de reiniciar. |
| Aplicativos | Rede, cache, renderização ou serviço remoto | Medir abrir e voltar após reinicialização, 5 repetições. |
| RAM e processos | Indeterminado | Só com diagnóstico autorizado e mecanismo oficial; não inferir de sintomas. |
| Animações | Custo de renderização | Comparar interface experimental em navegador/SDK, depois na TV se autorizada. |

Prioridade de mudanças sem tocar no firmware: interface experimental com DOM pequeno, sem animações e navegação direta por setas. Isso pode reduzir trabalho **na própria interface experimental**; não há evidência de que acelere Smart Hub, boot ou apps existentes. Nenhuma melhoria de CPU/RAM na TV foi medida.
