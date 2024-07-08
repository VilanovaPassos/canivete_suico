@echo off
for /f "delims=[] tokens=2" %%a in ('ping -4 -n 1 %computername%') do set IP=%%a

start http://%IP%
