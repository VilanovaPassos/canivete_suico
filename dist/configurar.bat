@echo para continuar voce deve ter o Holyrics instalado no seu disco C
pause

cd %~dp0

@echo Criando diretorio na pasta do holyrics .....
mkdir C:\Holyrics\Holyrics\files\dse-complementos\canivete

@echo Copiando Canivete para dentro do Holyrics ...
xcopy .\Canivete.exe C:\Holyrics\Holyrics\files\dse-complementos\canivete
xcopy .\ffmpeg.exe C:\Holyrics\Holyrics\files\dse-complementos\canivete
xcopy .\ffplay.exe C:\Holyrics\Holyrics\files\dse-complementos\canivete
xcopy .\ffprobe.exe C:\Holyrics\Holyrics\files\dse-complementos\canivete
xcopy .\yt-dlp.exe C:\Holyrics\Holyrics\files\dse-complementos\canivete
xcopy .\icon.ico C:\Holyrics\Holyrics\files\dse-complementos\canivete
xcopy .\PDF2JPG.png C:\Holyrics\Holyrics\files\dse-complementos\canivete
xcopy .\style.css C:\Holyrics\Holyrics\files\dse-complementos\canivete
xcopy .\VideoDownload.png C:\Holyrics\Holyrics\files\dse-complementos\canivete

@echo abrindo porta 80 ...
netsh advfirewall firewall add rule name="canivete_holyrics" protocol=TCP dir=in localport=80 action=allow
netsh advfirewall firewall add rule name="canivete_holyrics" protocol=TCP dir=out localport=80 action=allow

@echo Criando tarefa no agendador de tarefas ...
schtasks.exe /Create /ru SYSTEM /XML .\canivete_holyrics.xml /tn canivete

@echo Colocando pasta no PATH
setx PATH "%PATH%;C:\Holyrics\Holyrics\files\dse-complementos\canivete" /m

@echo executando tarefa pala primeira vez
schtasks /run /tn canivete

@echo instalacao concluida com sucesso!!
pause