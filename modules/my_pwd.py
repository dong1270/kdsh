import os

def printWorkingDir():
    #  현재 폴더 경로
    return os.getcwd()


def nowDir():
    return str(printWorkingDir().split('/')[-1])

