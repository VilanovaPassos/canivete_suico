@echo ATENÇAO!! Isto ira desisntalar o Canivete_1.0 de seu computador
pause

@echo.
@echo Deletando executavel
rmdir /s /q C:\Holyrics\Holyrics\files\dse-complementos\canivete

@echo.
@echo fechando portas
netsh advfirewall firewall delete rule name="canivete_holyrics"

@echo.
@echo apagando tarefa agendada
schtasks /delete /tn canivete

@echo Desinstalado com sucesso !!
pause
