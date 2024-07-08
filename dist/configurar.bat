@echo para continuar voce deve ter o Holyrics instalado no seu disco C
pause

cd %~dp0

@echo Copiando Canivete para dentro do Holyrics ...
xcopy .\Canivete_0.1.exe C:\Holyrics\Holyrics\files

@echo Criando tarefa no agendador de tarefas
schtasks.exe /Create /ru SYSTEM /XML .\canivete_holyrics.xml /tn canivete
pause