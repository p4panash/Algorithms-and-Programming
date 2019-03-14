from Domain.Plant import Plant

class PlantRepository:
    def __init__(self):
        self.__plantRepo = []

    def add_plant(self, plant):
        if self.does_already_exists(plant):
            raise ValueError("Repository: Plant already exists !")
        else:
            self.__plantRepo.append(plant)

    def does_already_exists(self, plant):
        for element in self.__plantRepo:
            if element.get_name() == plant.get_name():
                return True
        return False

    def calculate_price_for_plants_with_letter(self, letter):
        price = 0
        for element in self.__plantRepo:
            if element.is_starting_with_letter(letter):
                price += element.get_price() * element.get_quantity()
        return price

    def remove_out_of_stock(self):
        index = 0
        while index < len(self.__plantRepo):
            if self.__plantRepo[index].get_quantity() == 0:
                del self.__plantRepo[index]
            else:
                index += 1

    def __str__(self):
        string = ""
        for element in self.__plantRepo:
            string += str(element) + '\n'
        return string
