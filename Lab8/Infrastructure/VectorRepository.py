from Domain.MyVector import MyVector
import sys

class VectorRepository:
    def __init__(self):
        self.__repository = []

    def indexByName(self, name_id):
        for index in range (0, len(self.__repository)):
            if self.__repository[index].getNameID() == name_id:
                return index
        return -1

    def addVector(self, vector):
        if self.indexByName(vector.getNameID()) != -1:
            raise ValueError("Repository: Vector already exists !")
        self.__repository.append(vector)

    def getAllVectors(self):
        return self.__repository

    def getVectorAtIndex(self, index):
        if index < 0 and index >= len(self.__repository):
            raise ValueError("Repository: Index out of range")
        return self.__repository[int(index)]

    def updateVectorAtIndex(self, index, vector):
        if index < 0 and index >= len(self.__repository):
            raise ValueError("Repository: Index out of range")
        self.__repository[index].setNameID(vector.getNameID())
        self.__repository[index].setColour(vector.getColour())
        self._repository[index].setType(vector.getType())
        self._repository[index].setValues(vector.getValues())


    def updateVectorByName(self, name_id, vector):
        if self.indexByName(name_id) == -1:
            raise ValueError("Repository: There isn't a vector with that name_id")
        self.__repository[self.indexByName(name_id)].setColour(vector.getColour())
        self._repository[self.indexByName(name_id)].setType(vector.getType())
        self._repository[self.indexByName(name_id)].setValues(vector.getValues())

    def delVectorByIndex(self, index):
        if index < 0 and index > len(self.__repository):
            raise ValueError("Repository: Index out of range")
        del self.__repository[index]

    def delVectorByName(self, name_id):
        if self.indexByName(name_id) == -1:
            raise ValueError("Repository: There isn't a vector with that name_id")
        del self.__repository[self.indexByName(name_id)]

    def sumOfAllVectors(self):
        sum = 0
        for el in self.__repository:
            sum += el.sumOfElements()
        return sum

    def getMinSize(self):
        min = sys.maxsize
        for el in self.__repository:
            if len(el.getValues) < min:
                min = len(el.getValues)
        return min

    def getVectorOfSums(self):
        if len(self.__repository) == 0:
            raise ValueError("Repository: Empty repository")
        size = self.getMinSize()
        values = []
        for index in range(0, size):
            values.append(self.__repository[0].getValues()[index])
        vector = MyVector("sum", "r", 1, values)
        for index in range(1, len(self.__repository)):
            vector.addVector(self.__repository[index].getValues())
        return vector

    def getListOfVectorsWithSum(self, sum):
        vectorsList = []
        for el in self.__repository:
            if el.sumOfElements == sum:
                vectorsList.append(el)
        return vectorsList

    def getListOfVectorsWithMinLess(self, min):
        vectorsList = []
        for el in self.__repository:
            if el.minOfElements() < min:
                vectorsList.append(el)
        return vectorsList

    def sumOfElementsInVectorsWithColour(self, colour):
        sum = 0
        for el in self.__repository:
            if el.getColour == colour:
                sum += el.sumOfElements()
        return sum

    def getMaxOfAllVectorsWithSumGreater(self, sum):
        maxvalue = -sys.maxsize
        for el in self.__repository:
            if el.sumOfElements() > sum:
                maxvalue = max(maxvalue, el.maxOfElements())
        return maxvalue

    def getMinOfAllVectors(self):
        minvalue = sys.maxsize
        for el in self.__repository:
            minvalue = min(minvalue, el.minOfElements())
        return minvalue

    def getProdOfConsecutiveVectors(self):
        if len(self.__repository) == 0:
            raise ValueError("Repository: Empty repository")
        size = self.getMinSize()
        values = []
        for index in range(0, size):
            values.append(1)
        vector = MyVector("prod", "r", 1, values)
        for el in self.__repository:
            vector.multVector(el.getValues())
        return vector.getValues()

    def delAllRepository(self):
        del self.__repository[:]

    def delVectorsByColour(self, colour):
        index = 0
        while index <= len(self.__repository):
            if self.__repository[index].getColour == colour:
                del self.__repository[index]
            else:
                index += 1

    def delVectorsByProductGreater(self, value):
        index = 0
        while index <= len(self.__repository):
            if self.__repository[index].productOfElements() == value:
                del self.__repository[index]
            else:
                index += 1

    def delVectorsBetweenIndexes(self, start, end):
        if start < 0 or start >= len(self.__repository) or end < 0 or end >= len(self.__repository):
            raise ValueError("Repository: Index out of range")
        if end > start:
            del self.__repository[start:end]
        else:
            del self.__repository[end:start]

    def delVectorsByMaxValue(self, value):
        index = 0
        while index <= len(self.__repository):
            if self.__repository[index].maxOfElements == value:
                del self.__repository[index]
            else:
                index += 1

    def updateVectorsByAddingScalar(self, scalar):
        for el in self.__repository:
            el.addScalar(scalar)

    def updateVectorsColourByNameID(self, name_id, colour):
        for el in self.__repository:
            if el.getNameId() == name_id:
                    el.setColour(colour)

    def updateVectorsColourByType(self, type, colour):
        for el in self.__repository:
            if el.getType() == type:
                el.setColour(colour)
