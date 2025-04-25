import os, shutil

class removeDir() :
    def __init__(self, data="") :
        self.__target = data

    def execute(self) :
        try:
            if os.path.isfile(self.__target):
                os.remove(self.__target)
            else:
                os.rmdir(self.__target)
        except FileNotFoundError :
            print("can not found") 
        except PermissionError :
            print("permission denied")
        except OSError :
            print("this directory not empty")
    
    def rmAll(self) :
        try : 
            shutil.rmtree(self.__target)
        except FileNotFoundError:
            print('\'' + self.__target + '\'을 찾을 수 없습니다.')
        except PermissionError:
            print('삭제 권한이 없습니다.')
        