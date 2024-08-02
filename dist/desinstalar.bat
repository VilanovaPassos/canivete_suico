@echo ATENÇAO!! Isto ira desisntalar o Canivete_1.0 de seu computador
pause

@echo.
@echo apagando tarefa agendada
schtasks /f /end /tn canivete
schtasks /f /delete /tn canivete
schtasks /f /delete /tn abre_navegador
schtasks /f /delete /tn abre_video
schtasks /f /delete /tn abre_imagem
schtasks /f /delete /tn abre_audio

@echo tirando do path
setx /M PATH "%PATH:C:\Holyrics\Holyrics\files\dse-complementos\canivete;=%"

@echo.
@echo Deletando executavel
rmdir /s /q C:\Holyrics\Holyrics\files\dse-complementos\canivete

@echo.
@echo Deletando atalho
del /s /q C:\Users\Public\Desktop\CaniveteHolyrics.exe

@echo.
@echo fechando portas
netsh advfirewall firewall delete rule name="canivete_holyrics"

@echo Desinstalado com sucesso !!
pause
