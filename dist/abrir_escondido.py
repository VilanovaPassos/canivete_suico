import subprocess
import os

def startProgram():
    SW_HIDE = 0
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = SW_HIDE
    subprocess.Popen(os.path.join(os.path.dirname(__file__) or '.','Canivete_0.1.exe'), startupinfo=info)

if __name__ == "__main__":
    startProgram()