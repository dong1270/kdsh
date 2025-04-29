import subprocess

def addon(operator = "", operand = "", option = ""):
    filePath = "/Users/kangdongseong/myLib/kdsh/addon"
    moduelPath = "/Users/kangdongseong/myLib/kdsh/kdsh_addon/"
    cmd_list = open(filePath, mode='r')
    for cmd in cmd_list :
        if cmd == operator :
            cmd_list.close()
            subprocess.run(["python3", moduelPath + cmd + ".py"])
            
            return

    cmd_list.close()
    print("'" + operator + "' 명령을 찾을 수 없습니다.")