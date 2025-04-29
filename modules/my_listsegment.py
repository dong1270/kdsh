import os

def isHome(pathData):
    if pathData == '~':
        return os.environ['HOME']
    return pathData

class listSegment():
    __dir_context = "\033[94m"
    __text_tail = "\033[0m"
    
    def __init__(self, str1, str2) :
        self.__path   = isHome(str1)
        self.__option = str2
            
    def get_result(self):
        try : 
            dir_context = os.listdir(self.__path)
            for list_str in dir_context:
                if os.path.isdir(list_str) :
                    print(self.__dir_context + list_str + self.__text_tail)
                elif os.path.islink(list_str) :
                    print(self.__dir_context + list_str + self.__text_tail)
                else : 
                    print(list_str)
        except FileNotFoundError :
            return "can not found: " + self.__path + " "  + self.__option
        except PermissionError :
            return "Permission denied: " + self.__path + " " + self.__option
