import unittest
from Infrastructure.DepartmentRepository import DepartmentRepository
from Domain.Department import Department

class TestDepartmentRepository(unittest.TestCase):

    def test_add(self):
        repo = DepartmentRepository()
        repo.addDepartment(Department(1, "Accident and emergency", 100, []))
        repo.addDepartment(Department(1, "Anesthetics", 30, []))
        repo.addDepartment(Department(2, "Anesthetics", 30, []))
        self.assertEqual(repo.getDepartmentById(1), Department(1, "Accident and emergency", 100, []))
        self.assertEqual(repo.getDepartmentById(2), Department(2, "Anesthetics", 30, []))

    def test_findDepartmentById(self):
        repo = DepartmentRepository()
        repo.addDepartment(Department(1, "Accident and emergency", 100, []))
        repo.addDepartment(Department(4, "Anesthetics", 30, []))
        repo.addDepartment(Department(2, "Anesthetics", 30, []))
        self.assertEqual(repo.findDepartmentById(1), 0)
        self.assertEqual(repo.findDepartmentById(2), 2)

    def test_getDepartmentById(self):
        repo = DepartmentRepository()
        repo.addDepartment(Department(1, "Accident and emergency", 100, []))
        repo.addDepartment(Department(4, "Anesthetics", 30, []))
        self.assertEqual(repo.getDepartmentById(1), Department(1, "Accident and emergency", 100, []))

    def test_sortByPatientsNo(self):
        repo = DepartmentRepository()
        repo.addDepartment(Department(1, "Accident and emergency", 100, [1, 2, 3]))
        repo.addDepartment(Department(2, "Anesthetics", 30, []))
        repo.addDepartment(Department(3, "Cardiology", 30, [212, 2]))
        repo.sortByPatientsNo()

        test = [4, 2, 9, 14, 1]
        p = sorted(test)
        p[0] += 3
        print(test[4])