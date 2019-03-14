from Infrastructure.VectorRepository import VectorRepository
from Domain.MyVector import MyVector
class UI:
    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def showOptions():
        print(" 1. Add a vector to the repository\n 2. Get all vectors\n 3. Get a vector at a given index\n 4. Update a vector at a given index\n"
              +" 5. Update a vector identified by name_id\n 6. Delete a vector by index\n 7. Delete a vector by name_id\n 8. Plot all vectors in a chart based on the type and colour of each vector\n"
              +" 9. Get the sum of elements in all vectors\n 10. Get the vector which represents the sum of all vectors.\n 11. Get the list of vectors having a given sum of elements.\n 12. Get the list of vectors having the minimum less than a given value.\n"
              +" 13. Get the sum of all the elements in those vectors having a given colour.\n 14. Get the max of all vectors having the sum greater than a given value.\n 15. Get the min of all vectors.\n"
              +" 16. Get a list of values representing the multiplication of consecutive vectors in the repository.\n 17. Delete all vectors from the repository.\n 18. Delete all vectors for which the colour is a given value.\n"
              +" 19. Delete all vectors for which the product of elements is greater than a given value.\n 20. Delete all vectors that are between two given indexes.\n 21. Delete all vectors for which the max value is equal to a given value.\n"
              +" 22. Update all vectors by adding a given scalar to each element.\n 23. Update a vector identified by name _id.\n 24. Update the colour of a vector identified by name_id.\n 25. Update all vectors having a given type by setting their colour to the same given value.")

    @staticmethod
    def showVector(vector):
        print(vector)

    @staticmethod
    def showList(result):
        for el in result:
            print(el)

    @staticmethod
    def ReadArray():
        try:
            array = [int(x) for x in input("Introduce values: ").split(" ")]
        except ValueError:
            print("The array's elements must be integers")
        return array

    def run(self):
        self.showOptions()
        choice = int(input())
        while choice != 0:
            if choice == 1:
                name_id = input(" Introduce the id: ")
                colour = input(" Introduce colour: ")
                type = input(" Introduce type: ")
                values = self.ReadArray()
                self.__controller.addVector(name_id, colour, type, values)
            elif choice == 2:
                self.showList(self.__controller.getAllVectors())
            elif choice == 3:
                index = input("Introduce index: ")
                self.showVector(self.__controller.getVectorAtIndex(index))
            elif choice == 4:
                index = input(" Introduce the index: ")
                name_id = input(" Introduce the id: ")
                colour = input(" Introduce colour: ")
                type = input(" Introduce type: ")
                values = self.ReadArray()
                self.__controller.updateVectorAtIndex(index, name_id, colour, type, values)
            elif choice == 5:
                name_id = input(" Introduce the id: ")
                colour = input(" Introduce colour: ")
                type = input(" Introduce type: ")
                values = self.ReadArray()
                self.__controller.updateVectorByName(name_id, colour, type, values)
            elif choice == 6:
                index = input(" Introduce index")
                self.__controller.delVectorByIndex(index)
            elif choice == 7:
                name_id = input(" Introduce the name id: ")
                self.__controller.delVectorByName(name_id)
            elif choice == 8:
                self.__controller.plotAllVectors()
            elif choice == 9:
                print(str(self.__controller.sumOfAllVectors()))
            elif choice == 10:
                print(self.__controller.getVectorOfSums())
            elif choice == 11:
                try:
                    sum = int(input(" Introduce the value: "))
                    self.showList(self.__controller.getListOfVectorsWithSum(sum))
                except ValueError:
                    print(" Invalid data !")
            elif choice == 12:
                try:
                    min = int(input(" Introduce the value: "))
                    self.showList(self.__controller.getListOfVectorsWithMinLess(min))
                except ValueError:
                    print(" Invalid data !")
            elif choice == 13:
                try:
                    value = int(input(" Introduce colour: "))
                    print(self.__controller.sumOfElementsInVectorsWithColour(colour))
                except ValueError:
                    print( "Invalid data !")
            elif choice == 14:
                try:
                    sum = input(" Introduce the value: ")
                    print(self.__controller.getMaxOfAllVectorsWithSumGreater(sum))
                except ValueError:
                    print(" Invalid data !")
            elif choice == 15:
                print(self.__controller.getMinOfAllVectors())
            elif choice == 16:
                print(self.__controller.getProdOfConsecutiveVectors())
            elif choice == 17:
                self.__controller.delAllRepository()
            elif choice == 18:
                try:
                    colour = input(" Introduce colour: ")
                    self.__controller.delVectorsByColour(colour)
                except ValueError:
                    print(" Invalid data !")
            elif choice == 19:
                try:
                    value = input(" Introduce value: ")
                    self.__controller.delVectorsWithProductGreater(value)
                except ValueError:
                    print(" Invalid data !")
            elif choice == 20:
                try:
                    start = int(input(" Introduce the index of the starting point: "))
                    end = int(input(" Introduce the index of the end point: "))
                    self.__controller.delVectorsBetweenIndexes(start, end)
                except ValueError:
                    print(" Invalid data !")
            elif choice == 21:
                try:
                    value = int(input(" Introduce value: "))
                    self.__controller.delVectorsByMaxValue(value)
                except ValueError:
                    print(" Invalid data !")
            elif choice == 22:
                try:
                    scalar = int(input(" Introduce the scalar: "))
                    self.__controller.updateVectorsByAddingScalar(scalar)
                except ValueError:
                    print(" Invalid data !")
            elif choice == 23:
                name_id = input(" Introduce the id: ")
                colour = input(" Introduce colour: ")
                type = input(" Introduce type: ")
                values = self.ReadArray()
                self.__controller.updateVectorByName(name_id, colour, type, values)
            elif choice == 24:
                try:
                    colour = input(" Introduce the colour: ")
                    name_id = input(" Introduce name_id: ")
                    self.__controller.updateVectorsColourByNameID(name_id, colour)
                except ValueError:
                    print(" Invalid data !")
            elif choice == 25:
                try:
                    type = int(input(" Introduce the type: "))
                    colour = input(" Introduce the colour: ")
                    self.__controller.updateVectorsColourByType(type, colour)
                except ValueError:
                    print("Invalid data !")
            self.showOptions()
            choice = int(input())
