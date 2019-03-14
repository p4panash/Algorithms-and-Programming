from Domain.Contact import Contact

class ContactController:
    def __init__(self, repo):
        self.__contactRepo = repo

    def addContact(self, name, phone_number, type):
        try:
            contact = Contact(name, phone_number, type)
            self.__contactRepo.addContact(contact)
        except ValueError as ex:
            return ex
        return ""

    def getContactList(self):
        result = ""
        for el in self.__contactRepo.getRepo():
            result += str(el) + "\n"
        return result

    def mySearch(self):
        result = ""
        for el in self.__contactRepo.getContactsEndingWith999MySearch():
            result += str(el) + "\n"

    def pythonFilter(self):
        result = ""
        for el in self.__contactRepo.getContactsEndingWith999search():
            result += str(el) + "\n"
