from Domain.Plant import Plant
from Infastructure.PlantRepository import PlantRepository

class UI:
    def __init__(self, repo):
        self.__repo = repo

    @staticmethod
    def print_options():
        print(" 1. Add plant \n 2. Calculate the total price for all the plants with name starting with a given letter \n 3. Remove all plants for each the quantity is zero \n 4. Print all plants \n 5. Exit")

    @staticmethod
    def read_plant():
        name = str(input("Introduce name: "))
        price = int(input("Introduce price: "))
        quantity = int(input("Introduce quantity: "))
        return Plant(name, price, quantity)

    def add_plant(self):
        try:
            self.__repo.add_plant(self.read_plant())
        except ValueError as e:
            print("Error" + str(e))
            self.add_plant()

    def calculate_price(self):
        letter = input("Introduce letter: ")
        return self.__repo.calculate_price_for_plants_with_letter(letter)

    def remove_plants(self):
        self.__repo.remove_out_of_stock()

    def print_plants(self):
        print(self.__repo)


    def run(self):
        self.print_plants()
        self.print_options()
        option = int(input())
        while option != 5:
            if option == 1:
                self.add_plant()
            elif option == 2:
                print("The total price is " + str(self.calculate_price()))
            elif option == 3:
                self.remove_plants()
            elif option == 4:
                self.print_plants()
            self.print_options()
            option = int(input())