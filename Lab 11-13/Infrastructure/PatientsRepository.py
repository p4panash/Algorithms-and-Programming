class PatientsRepository:

    def __init__(self):
        self.__patientsRepo = []

    def addPatient(self, patient):
        if self.getPatientByID(patient.getPersonalNumericalCode()) == -1:
            self.__patientsRepo.append(patient)

    def getPatientByID(self, id):
        for index, el in enumerate(self.__patientsRepo):
            if el.getPersonalNumericalCode() == id:
                return index
        return -1

    def updatePatientByID(self, id, patient):
        index = self.getPatientByID(id)
        if index != -1:
            self.__patientsRepo[index] = patient

    def removePatientByID(self, id):
        index = self.getPatientByID(id)
        if index != -1:
            del self.__patientsRepo[index]

    def getPatientsRepository(self):
        return self.__patientsRepo

    def delPatientsReposiotry(self):
        del self.__patientsRepo[:]

    def __str__(self):
        repoStr = ""
        for el in self.__patientsRepo:
            repoStr += str(el) + "\n"
        return repoStr