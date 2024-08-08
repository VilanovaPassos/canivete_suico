# Canivete suiço para holyrics

Ferramenta criada para ultilizar jutamente com holyrics, tornando facil o download e conversão de diferentes tipos de arquivos de midia integrando o resultado direto com o holyrics. Versão .1.4.1 conta com downloader de videos do youtube, com opção de baixar tanto video quanto somente o audio diretamente para as respectivas pastas do holyrics. Conversor de PDF para imagem, salvando em uma pasta com o mesmo nome do arquivo direto na pasta de imagem do holyrics. Conversor de videos para mp3, salvando direto na pasta do Holyrics.

Esta nova versão tambem conta com a possibilidade de estar acessando por um celular conectado na mesma rede atraves de um QR code.

## Como Instalar:
É preciso primeiro ter o Holyrics instalado no disco C do seu computador isto é C:\Holyrics

### Instalador:
Baixe o instalador canivete_holyrics_installer.exe disponivel na ultima release e execute em seu computador, o programa sera instalado e um atalho sera criado na sua area de trabalho.

### Manual com arqivos de lote :
Baixe a pasta zipada contendo todos os arquivos necessarios para a instalação na ultima release, abra a pasta e execute cofigurar.bat como administrador, isso copiara o programa Canivete.exe e suas dependecias para dentro da pasta do holyrics e criara uma tarefa no agendador de tarefas, fazendo com que o programa inicie automaticamente sempre que o computador for ligado.

Voce pode usar o programa via navegador digitando localhost na barra de URL ou clicando no atalho criado em sua area de trabalho que iniciara seu navegador padrao já na aplicação.

### Desinstalar :
A desinstalacao pode ser feita executando o arquivo desisntalar.bat como administrador, isso apagara o programa Canivete.exe e suas dependencias da pasta do holyrics e apagara as taefas do agendador de tarefas. Recomendo que seja feita a desisntalacao antes de testar uma nova versao

## Como usar:
Por padrão desde a instalação o programa iniciara junto com o computador, para acessar a interface basta clicar no atalho ou digitar localhost na barra de endereço do seu navegador.

### Donloader YouTube:
Com a aplicação aberta no navegador, basta colar a URL do video do youtube e clicar em baixar, o video sera baixado em 720p por padrao na pasta de videos do holirycs. Selecionando a opção "somente audio" o programa baixara somente o audio do video e ira salvar na pasta de audios do holyrics.

Com a opção "Abrir a pasta apos o Download" na posição "sim", o programa ira abrir a pasta do hollyrics na qual o arquivo foi baixado.

Na aba "avançado" voce pode escolher a resolução em que o video sera baixado, entretanto essa opçao ira aumentar significativamente o tempo de dowload, pois o arquivo final precisará ser renderizado. Dependendo do seu computador e do tamanho do video pode levar algumas horas, por isso seu uso não é recomendado.

### Conversor PDF --> imagem:
Com a aplicação aberta no navegador, na aba "Conversor PDF" basta clicar na caixa de seleção de arquivos e escolher o arquivo, ou arrastar o arquivo para a caixa e clicar em converter, as paginas do PDF serão convertidas em imagens e salvas numa pasta com o mesmo nome do PDF na pasta de imagens do holirycs. 

Com a opção "Abrir a pasta apos o conversão" na posição "sim", o programa ira abrir a pasta do hollyrics na qual o arquivo foi baixado.

### Conversor Video --> mp3:
Com a aplicação aberta no navegador, na aba "Conversor mp3" basta clicar na caixa de seleção de arquivos e escolher o arquivo, ou arrastar o arquivo para a caixa e clicar em converter, o video sera convertido para audio e salvo como mp3 na pasta de audios do holirycs. 

Com a opção "Abrir a pasta apos o conversão" na posição "sim", o programa ira abrir a pasta do hollyrics na qual o arquivo foi baixado.

### QR CODE CELULAR
Com o celular conectado na mesma rede (WI-FI) em que o computador que esta rodando o programa, a interface pode ser acessada atraves de um QR CODE, basta clicar na aba de QR Code e escanear com a camera. Com o celular e pssivel enviar arquivos para serem convertidos. Os arquivos baixados e convertidos sempre serão salvos no computador em que esta rodando o programa, em sua respectiva pasta dentro do Holyrics.

### LOGS
Na aba Logs é possivel visualizar os logs das operações feitas pelo programa em tempo real.