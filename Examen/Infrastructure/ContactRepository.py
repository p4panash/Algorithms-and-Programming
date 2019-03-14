from Utils.Utils import mysearch

class ContactRepository:
    def __init__(self):
        self.__repo = []

    def addContact(self, contact):
        self.__repo.append(contact)

    def getRepo(self):
        return self.__repo

    def getContactsEndingWith999MySearch(self):
        return mysearch(self.__repo, lambda x: x.isEndingIn("999") == True)

    def getContactsEndingWith999search(self):
        return list(filter(lambda x: x.isEndingIn("999") == True, self.__repo))