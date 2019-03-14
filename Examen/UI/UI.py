class UI:
    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def showOptions():
        print (" 1. Add contact \n 2. Get all contacts which phone number ends with 999 my search " \
               "\n 3. Get all contacts which phone number ends with 999 python search \n 4. Show contacts \n 9. Exit")

    def run(self):
        option = -1
        while option != 9:
            print(self.__controller.getContactList())
            self.showOptions()
            option = int(input("Your option is: "))
            if option == 1:
                name = input("Introduce the contact name: ")
                phone_number = input("Introduce phone number: ")
                type = input("Introduce type(work / personal): ")
                message = self.__controller.addContact(name, phone_number, type)
                if message != "":
                    print(message)
            elif option == 2:
                print(self.__controller.mySearch())
            elif option == 3:
                print(self.__controller.pythonFilter())
            elif option == 4:
                print(self.__controller.getContactList())
            elif option != 9:
                print("Invalid option ! Please try again !")
