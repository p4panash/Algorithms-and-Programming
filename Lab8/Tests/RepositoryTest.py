import unittest
from Domain.MyVector import MyVector
from Infrastructure.VectorRepository import VectorRepository

class RepositoryTest(unittest.TestCase):

    def test_addVector(self):
        repo = VectorRepository()
        repo.addVector(MyVector("prim", "r", 1, [1, 2]))
        self.assertEqual(repo.getAllVectors()[0], MyVector("prim", "r", 1, [1, 2]))
        try:
            repo.addVector(MyVector("prim", "g", 3, [1, 2, 3, 4]))
            assert False
        except:
            assert True

    def test_getAllVectors(self):
        repo = VectorRepository()
        repo.addVector(MyVector("1", "r", 2, [1, 2, 3]))
        repo.addVector(MyVector("12", "g", 1, [123, 211, 332]))
        repo.addVector(MyVector("311", "b", 4, [2, 1, 3]))


if __name__ == "__main__":
    unittest.main()

