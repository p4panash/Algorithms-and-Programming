import Utils.Utils as utils

class Department:

    def __init__(self, id, name, number_of_beds, patients):
        self.__id = id
        self.__name = name
        self.__number_of_beds = number_of_beds
        self.__patients = patients

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setNumberOfBeds(self, number_of_beds):
        self.__number_of_beds = number_of_beds

    def getNumberOfBeds(self):
        return self.__number_of_beds

    def getPatients(self):
        return self.__patients

    def setPatients(self, patients):
        self.__patients == patients

    def getNumberOfPatients(self):
        return len(self.__patients)

    def getNumberOfPatientsAgeOver(self, age):
        return len(utils.mySearch(self.__patients, lambda x: x.getAge() > age))

    def getNumberOfPatientsAgeUnder(self, age):
        return len(utils.mySearch(self.__patients, lambda x: x.getAge() < age))

    def getPatientById(self, id):
        for index, el in enumerate(self.__patients):
            if el.getPersonalNumericalCode() == id:
                return index
        return -1

    def sortPatientsAlphabetically(self):
        self.__patients = utils.mySort(self.__patients, lambda x, y: x.getFirstName() < y.getLastName())

    def sortPatientsByPNC(self):
        self.__patients = utils.mySort(self.__patients,
                                           lambda x, y: x.getPersonalNumericalCode() < y.getPersonalNumericalCode())

    def addPatient(self, patient):
        if len(self.__patients) < self.__number_of_beds:
            if self.getPatientById(patient.getPersonalNumericalCode()) == -1:
                self.__patients.append(patient)
            else:
                raise ValueError("Patient already exist !")
        else:
            raise ValueError("Department is full !")

    def getPatientsWithString(self, string):
        return utils.mySearch(self.__patients, lambda x: string in x.getFirstName() or string in x.getLastName())

    def getPatientsWithFirstName(self, name):
        return utils.mySearch(self.__patients, lambda x: name == x.getFirstName())

    def groupPatientsByDisease(self, k):

        def c1(sol, myList):
            for i in range(len(sol) - 1):
                if myList[sol[i]].getPersonalNumericalCode() != myList[sol[len(sol) - 1]].getPersonalNumericalCode():
                    return False
            return True

        myList = self.__patients
        constraints = [c1]
        aux = []
        for el in utils.myBacktracking(k, myList, constraints):
            aux.append(self.constructSolution(el, myList))
        if aux == []:
            return "This department doesnt have valid patients for grouping."
        return aux

    def __str__(self):
        patientsStr = "\n"
        for index, el in enumerate(self.__patients):
            patientsStr += str(index) + " " + str(el) + '\n'
        return str(self.__id) + " " + str(self.__name) + " " + str(self.__number_of_beds) + patientsStr

    def __eq__(self, other):
        if (self.__id == other.getId() and self.__name == other.getName() and
                self.__number_of_beds == other.getNumberOfBeds() and self.__patients == other.getPatients()):
            return True
        return False


