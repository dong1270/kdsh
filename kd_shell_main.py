# project: 강동_shell
# description: 사용자와 서버 사이에 상호작용할 인터페이스(혹은 쉘)

# 1. 기본적인 기능: ls(v), cd(v), pwd(v), mkdir(v), rm
# 2. 서버에서 작동할 명령어 작성
#!/usr/bin/python
#-*- coding: utf-8 -*-
import argparse, sys
import time
from modules.my_addon import addon
from modules.my_install import installer

from modules.my_changedir import changeDir
from modules.my_changedir import startShell
from modules.my_pwd import *
from modules.my_screenClear import screenClear


# from modules.my_listsegment import listSegment
from modules.my_listsegment import listSegment
from modules.my_mkdir import makeDirectory
from modules.my_remove import removeDir



def get_arguments():
    # parser = argparse.ArgumentParser()


    argv = sys.argv
    if len(argv) > 1 :
        command = argv[1]
    else :
        command = ""

    return command

def printFace():
    msg = open('./face', mode='r')
    text = ""
    for line in msg.readlines():
        text += line
    
    print("\033[94m" + text + "\033[0m")
    print()
    msg.close()

def printIssue():
    msg = open('./issue', mode='r')
    text = ""
    for line in msg.readlines():
        text += line
    
    print(text)
    print("현재 시간 : " + time.strftime('%y.%m.%d - %H:%M') + "\n")

    msg.close()

def main():
    startShell()
    while True:
        nowPosition = nowDir()
        operator = operand = option = " "
        
        print("[" + str(nowPosition) + "] >", end = ' ', flush=True)
        
        command = sys.stdin.readline().rstrip().split()

        if len(command) == 0:
            operator = " "
        if len(command) >= 1 :
            operator = command[0]
        if len(command) > 1 :
            operand = command[1] 
        if len(command) > 2 :
            option = command[2]

        if operator == "종료" or operator == "나가기":
            print("\n안녕히 가세요\n")
            break

        match operator :
            case '위치' : 
                print(printWorkingDir())
            case '새로고침' :
                screenClear()
            case '이동' :
                nowPosition = changeDir(operand)
            case '목록' :
                if operand == " " :
                    operand = '.'
                elif operand[0] == '-' :
                    if option == " " :
                        option = '.'
                    tmp = operand
                    operand = option
                    option = tmp

                if option[0] == '-':
                    if len(option) == 1:
                        print('잘못된 설정입니다.')
                else:
                    ls = listSegment(operand, option)
                    ls.get_result()
            case '만들기':
                mkdir = makeDirectory(operand)
                mkdir.execute()
            case '삭제':
                if operand[0] == '-' :
                    tmp = operand
                    operand = option
                    option = tmp

                rmdir = removeDir(operand)
                
                if option == '-전부':
                    rmdir.rmAll()
                else:
                    rmdir.execute()
            case ' ':
                print("", end='')
            case '설치':
                installer()               
            case _:
                addon(operator, operand, option)
                

if __name__ == '__main__':
    command = get_arguments()
    if(command == ""):
        os.system('chcp 65001')
        screenClear()
        printFace()
        printIssue()
        main()
    else:
        print(command)