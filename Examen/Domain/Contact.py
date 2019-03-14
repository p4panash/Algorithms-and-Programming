class Contact:
    def __init__(self, name, number, type):
        if name == "":
            raise ValueError("The contact name shouldn't be empty !")
        self.__name = name
        self.__number = number
        #if type != "work" or type != "personal":
            #raise ValueError("Invalid contact category !")
        self.__type = type

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    def getType(self):
        return self.__type

    def isEndingIn(self, endingDigits):
        if self.__number[11:] == endingDigits:
            return True
        return False

    def __str__(self):
        return self.__type + ": " + self.__name + " " + self.__number