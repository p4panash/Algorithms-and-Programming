from Utils.Utils import SmallerValue

class MyVector:

    def __init__(self, name_id, colour, type, values):
        if isinstance(name_id, str):
            self.__name_id = name_id
        else:
            raise ValueError("Domain: Name id isn't a string !")
        if colour in ['r', 'g', 'b', 'y', 'm']:
           self.__colour = colour
        else:
            raise ValueError("Domain: Wrong colour !")
        if isinstance(type, int):
            self.__type = type
        else:
            raise ValueError("Domain: Type should be an integer !")
        if isinstance(values, list):
            self.__values = values
        else:
            raise ValueError("Domain: Values isn't a list of numbers !")

    def setNameID(self, name_id):
        if isinstance(name_id, str):
            self.__name_id = name_id
        else:
            raise ValueError("Domain: Name id isn't a string !")

    def setColour(self, colour):
        if colour in ['r', 'g', 'b', 'y', 'm']:
           self.__colour = colour
        else:
            raise ValueError("Domain: Wrong colour !")

    def setType(self, type):
        if isinstance(type, int):
            self.__type = type
        else:
            raise ValueError("Domain: Type should be an integer !")

    def setValues(self, values):
        if isinstance(values, list):
            self.__values = values
        else:
            raise ValueError("Domain: Values isn't a list of numbers !")

    def getNameID(self):
        return self.__name_id

    def getColour(self):
        return self.__colour

    def getType(self):
        return self.__type

    def getValues(self):
        return self.__values

    def addScalar(self, scalar):
        for index in range(0, len(self.__values)):
            self.__values[index] += scalar

    def addVector(self, vector):
        for index in range(0, SmallerValue(len(self.__values), len(vector))):
            self.__values[index] += vector[index]

    def subVector(self, vector):
        for index in range(0, SmallerValue(len(self.__values), len(vector))):
            self.__values[index] -= vector[index]

    def multVector(self, vector):
        for index in range(0, SmallerValue(len(self.__values), len(vector))):
            self.__values[index] *= vector[index]

    def sumOfElements(self):
        return sum(self.__values)

    def averageOfElements(self):
        return sum(self.__values)/(len(self.__values))

    def productOfElements(self):
        product = 1
        for el in self.__values:
            product *= el
        return product

    def minOfElements(self):
        return min(self.__values)

    def maxOfElements(self):
        return max(self.__values)

    def __str__(self):
        return (str(self.__name_id) + " " + str(self.__colour) + " " +
            str(self.__type) + " " + str(self.__values))

    def __eq__(self, other):
        if (self.__name_id == other.getNameID() and self.__values == other.getValues() and
            self.__colour == other.getColour() and self.__type == other.getType()):
            return True
        return False
