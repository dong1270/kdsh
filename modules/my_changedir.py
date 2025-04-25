import os
from modules.my_pwd import nowDir

def startShell():
    os.chdir(os.environ['HOME'])

def changeDir(path):
    if path == "~":
        path = os.environ['HOME']
    try :
        os.chdir(path)
        print("now position is: " + os.getcwd())
    except PermissionError :
        print('접근권한이 없습니다.')
    except FileNotFoundError :
        print("\"" + path + "\"해당 디렉토리를 찾을 수 없습니다.")
    return nowDir()
