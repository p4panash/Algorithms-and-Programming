import Utils.Utils as utils

class DepartmentRepository:

    def __init__(self):
        self.__departmentRepo = []

    def addDepartment(self, department):
        if self.findDepartmentById(department.getId()) == -1:
            self.__departmentRepo.append(department)

    def findDepartmentById(self, id):
        for index, el in enumerate(self.__departmentRepo):
            if el.getId() == id:
                return index
        return -1

    def getDepartmentById(self, id):
        index = self.findDepartmentById(id)
        if index != -1:
            return self.__departmentRepo[index]

    def findPatientsInDepartment(self, cnp):
        def findPatient(department):
            return utils.mySearch(department.getPatients(), lambda x: x.getPersonalNumericalCode() == cnp)

        return utils.mySearch(self.__departmentRepo,lambda x: len(findPatient(x)) > 0)

    def updateDepartmentById(self, id, department):
        index = self.findDepartmentById(id)
        if index != -1:
            self.__departmentRepo[index] = department

    def removeDepartmentById(self, id):
        index = self.findDepartmentById(id)
        if index != -1:
            del self.__departmentRepo[index]

    def getDepartmentRepository(self):
        return self.__departmentRepo

    def delRepository(self):
        del self.__departmentRepo[:]

    def sortByPatientsNo(self):
        utils.mySort(self.__departmentRepo, lambda x, y: x.getNumberOfPatients() < y.getNumberOfPatients())

    def sortByPatientsAgeOver(self, age):
        utils.mySort(self.__departmentRepo,
                         lambda x, y: x.getNumberOfPatientsAgeOver(age) < y.getNumberOfPatientsAgeOver(age))

    def sortPatientsByNumberAndAlpha(self):
        for patients in self.__departmentRepo:
            patients.sortPatientsAlphabetically()
        utils.mySort(self.__departmentRepo, lambda x, y: x.getNumberOfPatients() < y.getNumberOfPatients())

    def findByPatientsAge(self, age):
        return utils.mySearch(self.__departmentRepo, lambda x: x.getNumberOfAgeUnder(age) > 0)

    def findDepartmentsByFirstName(self, name):
        return utils.mySearch(self.__departmentRepo, lambda x: len(x.getPatientsWithFirstName(name)) > 0)

    def groupDepartments(self, k, p):
        def c1(sol, myList):
            d = myList[sol[len(sol) - 1]]
            if self.groupPatientsByDisease(p, d) == "This department doesnt have valid patients for grouping.":
                return False
            return True

        def c2(sol, myList):
            for i in range(len(sol) - 1):
                if myList[sol[i]].getName() == myList[sol[len(sol) - 1]].getName():
                    return False
            return True

        myList = self.__data
        constraints = [c1, c2]
        aux = []

        for el in utils.myBacktracking(k, myList, constraints):
            aux.append(self.constructSolution(el, myList))

        if aux == []:
            return "This repository doesnt have valid departments for grouping."
        return aux

    def __str__(self):
        repoStr = ""
        for el in self.__departmentRepo:
            repoStr += str(el)
        return repoStr
