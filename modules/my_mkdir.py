import os

class makeDirectory():
    def __init__(self, dirName):
        # self.path       = data
        self.__dir_name   = dirName

    def execute(self):
        if self.__dir_name == " " :
            print("plz set name")
        else :
            try:
                os.makedirs(self.__dir_name)
            except PermissionError:
                print("permission denied")

