import platform
import os

def screenClear():
    if platform.system() == "windows" :
        os.system('cls')
    else:
        os.system('clear')