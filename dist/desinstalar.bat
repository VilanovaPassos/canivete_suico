@echo ATENÇAO!! Isto ira desisntalar o Canivete_1.0 de seu computador
pause

@echo.
@echo Deletando executavel
del C:\Holyrics\Holyrics\files\Canivete.exe
del C:\Holyrics\Holyrics\files\ffmpeg.exe
del C:\Holyrics\Holyrics\files\ffplay.exe
del C:\Holyrics\Holyrics\files\ffprobe.exe
del C:\Holyrics\Holyrics\files\yt-dlp.exe

@echo.
@echo fechando portas
netsh advfirewall firewall delete rule name="canivete_holyrics"

@echo.
@echo apagando tarefa agendada
schtasks /delete /tn canivete
