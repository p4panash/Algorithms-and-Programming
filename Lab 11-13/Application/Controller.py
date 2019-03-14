from Domain.Patients import Patients
from Domain.Department import Department
from Infrastructure.DepartmentRepository import DepartmentRepository
from Infrastructure.PatientsRepository import PatientsRepository

class Controller:

    def __init__(self, patientsRepo, departmentRepo):
        self.__patientsRepo = patientsRepo
        self.__departmentRepo = departmentRepo

    def getPatientsRepo(self):

        return self.__patientsRepo

    def getDepartmentRepo(self):
        return self.__departmentRepo

    @staticmethod
    def createPatient(first_name, last_name, cnp, disease):
        p = Patients(first_name, last_name, cnp, disease)
        return p

    @staticmethod
    def createDepartment(id, name, number, beds, l):
        l2 = []
        for el in l:
            p = Controller.createPatient(el[0], el[1], el[2], el[3])
            l2.append(p)

        d = Department(id, name, number, beds, l2)
        return d

    def addPatient(self, first_name, last_name, cnp, disease):
        p = self.createPatient(first_name, last_name, cnp, disease)
        self.__patientsRepo.addNew(p)

    def addDepartment(self, id, name, number, beds, l):
        d = self.createDepartment(id, name, number, beds, l)

        self.__departmentRepo.addDepartment(d)
        self.addListOfPatients(d.getPatients())

    def addListOfPatients(self, list):
        for el in list:
            if self.__patientsRepo.getPatientByID(el.getPersonalNumericalCode()) == -1:
                self.__patientsRepo.addPatient(el)

    def getPatientById(self, id):
        return self.__patientsRepo.getPatientByID(id)

    def getDepartmentById(self, id):
        return self.__departmentRepo.getDepartmentById(id)

    def updatePatientById(self, first_name, last_name, cnp, disease):
        newP = self.createPatient(first_name, last_name, cnp, disease)

        aux = self.__departmentRepo.findPatientsInDepartment(cnp)
        for el in aux:
            index = el.findPatientsInDepartment(cnp)
            if len(index) > 0:
                self.__departmentRepo.getDepartmentById(el.getId()).getPatientById(index[0].getPersonalNumericalCode()).update(first_name, last_name, disease)

        self.__patientsRepo.updatePatientByIndex(cnp, newP)

    def updateDepartmentById(self, name, number, beds, l, id):
        d = self.createDepartment(name, number, beds, l)
        self.__departmentRepo.updateDepartmentById(id, d)

    def showPatientRepo(self):
        return str(self.__patientsRepo)

    def showDepartmentRepo(self):
        return str(self.__departmentRepo)

    def clearRepos(self):
        self.__departmentRepo.delRepository()
        self.__patientsRepo.delRepository()

    def sortPatientByCnpCommand(self, id):
        self.__departmentRepo.getDepartmentById(id).sortPatientsByPNC()

    def sortPatientByPNC(self, id):
        return self.__departmentRepo.getDepartmentById(id).sortPatientsByPNC()

    def sortPatientsAlpha(self):
        return self.__departmentRepo.getDepartmentById(id).sortPatientsAlphabetically()

    def groupPatientsByDiseaseCommand(self, k, id):
        if k <= 0:
            raise Exception("Group size is not valid! <= 0")
        return self.__departmentRepo.getDepartmentById(id).groupPatientsByDisease(k)

    def groupDepartmentsCommand(self, k, p):
        if k <= 0 or p < 1:
            raise Exception("Group size or most patients number is not valid! <= 0")
        return self.__departmentRepo.groupDepartments(k, p)
