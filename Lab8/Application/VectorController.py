from Infrastructure.VectorRepository import VectorRepository, MyVector
class VectorController:
    def __init__(self, repository):
        self.__repository = repository

    def addVector(self, name_id, colour, type, values):
        try:
            vector = MyVector(name_id, colour, type, values)
            self.__repository.addVector(vector)
        except ValueError as ex:
            return "Error " + str(ex)

    def getAllVectors(self):
        return self.__repository.getAllVectors()

    def updateVectorAtIndex(self, index, name_id, colour, type, values):
        try:
            vector = MyVector(name_id, colour, type, values)
            self.__repository.addVectorAtIndex(index, vector)
        except ValueError as ex:
            print("Error " + str(ex))

    def getIndexByName(self, name_id):
        if not isinstance(name_id, str):
            raise ValueError("Controller: Name id isn't a string !")
        return self.__repository.indexByName(name_id)

    def updateVectorByName(self, name_id, colour, type, values):
        try:
            vector = MyVector(name_id, colour, type, values)
            self.__repository.updateVectorByName(vector.getNameID(), vector)
        except ValueError as ex:
            print("Error " + str(ex))

    def delVectorByIndex(self, index):
        try:
            self.__repository.delVectorByIndex(index)
        except ValueError as ex:
            print("Error " + str(ex))

    def sumOfAllVectors(self):
        return self.__repository.sumOfAllVectors()

    def getMinSize(self):
        return self.__repository.getMinSize()

    def getVectorOfSums(self):
        return self.__repository.getVectorOfSums()

    def getListOfVectorsWithSum(self, sum):
        if not isinstance(sum, int):
            raise ValueError("Controller: Input isn't a integer !")
        return self.__repository.getListOfVectorsWithSum(sum)

    def getListOfVectorsWithMinLess(self, min):
        if not isinstance(min, int):
            raise ValueError("Controller: Input isn't a integer !")
        return self.__repository.getListOfVectorsWithMinLess(min)

    def sumOfElementsInVectorsWithColour(self, colour):
        if not isinstance(colour, str):
            raise ValueError("Controller: Input isn't a string !")
        return self.__repository.sumOfElementsInVectorsWithColour(colour)

    def getMaxOfAllVectorsWithSumGreater(self, sum):
        if not isinstance(sum, int):
             raise ValueError("Controller: Input isn't a integer !")
        return self.__repository.getMaxOfAllVectorsWithSumGreater(sum)

    def getMinOfAllVectors(self):
        return self.__repository.getMinOfAllVectors()

    def getProdOfConsecutiveVectors(self):
        try:
            return self.__repository.getProdOfConsecutive()
        except ValueError as ex:
            print("Error " + str(ex))

    def delAllRepository(self):
        self.__repository.delAllRepository()

    def delVectorsByColour(self, colour):
        if not isinstance(colour, str):
            raise ValueError("Controller: Input isn't a string !")
        self.__repository.delVectorsByColour(colour)

    def delVectorsBetweenIndexes(self, start, end):
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Controller: Invalid start index or end index !")
        self.__repository.delVectorsBetweenIndexes(start, end)

    def delVectorsWithProductGreater(self, value):
        if not isinstance(value, int):
            raise ValueError("Controller: Value isn't a integer !")
        self.__repository.delVectorsByProductGreater(value)

    def delVectorsByMaxValue(self, value):
        if not isinstance(value, int):
            raise ValueError("Controller: Value isn't a integer !")
        self.__repository.delVectorsByMaxValue(value)

    def updateVectorsColourByNameID(self, name_id, colour):
        if not isinstance(name_id, str) or not isinstance(colour, str):
            raise ValueError("Controller: Invalid name_id or colour !")
        self.__repository.updateVectorsColourByNameID(name_id, colour)

    def updateVectorsByAddingScalar(self, scalar):
        if not isinstance(scalar, int):
            raise ValueError("Controller: Scalar isn't a integer !")
        self.__repository.updateVectorByAddingScalar(scalar)

    def updateVectorsColourByType(self, type, colour):
        if not isinstance(type, int) or not isinstance(colour, str):
            raise ValueError("Controller: Invalid type or colour !")
        self.__repository.updateVectorsColourByType(type, colour)

    def plotAllVectors(self):
        a = 1
