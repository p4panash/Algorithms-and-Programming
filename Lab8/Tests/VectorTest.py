import unittest
from Domain.MyVector import MyVector


class VectorTest(unittest.TestCase):

    def test_create(self):
        vector = MyVector("abcd", "r", 1, [1, 2, 3, 4])
        self.assertEqual(vector.getNameID(), "abcd")
        self.assertEqual(vector.getColour(), 'r')
        self.assertEqual(vector.getType(), 1)
        self.assertEqual(vector.getValues(), [1, 2, 3, 4])

        try:
            vector = MyVector(123, "r", 1, "1, 2, 3, 4")
            assert False
        except:
            assert True

        try:
            vector2 = MyVector("abcd", "g", 1, [1, 2, 3, 4])
            assert False
        except :
            assert True

    def test_setNameID(self):
        vector = MyVector("abcd", "r", 1, [1, 2, 3, 4])
        vector.setNameID("abc")
        self.assertEqual(vector.getNameID(), "abc")
        vector.setNameID("a")
        self.assertEqual(vector.getNameID(), "a")
        vector.setNameID("1234")
        self.assertEqual(vector.getNameID(), "1234")
        try:
            vector.setNameID(1234)
            assert False
        except:
            assert True
        vector.setNameID("AnAnas")
        self.assertEqual(vector.getNameID(), "AnAnas")

    def test_setColour(self):
        vector = MyVector("abcd", "r", 1, [1, 2, 3, 4])
        vector.setColour("g")
        self.assertEqual(vector.getColour(), "g")
        vector.setColour("b")
        self.assertEqual(vector.getColour(), "b")
        try:
            vector.setColour("n")
            assert False
        except:
            assert True

    def test_setType(self):
        vector = MyVector("abcd", "r", 1, [1, 2, 3, 4])
        vector.setType(3)
        self.assertEqual(vector.getType(), 3)
        vector.setType(5)
        self.assertEqual(vector.getType(), 5)
        try:
            vector.setType("a")
            assert False
        except:
            assert True

    def test_setValues(self):
        vector = MyVector("abcd", "r", 1, [1, 2, 3, 4])
        vector.setValues([1, 2, 3, 4, 5])
        self.assertEqual(vector.getValues(), [1, 2, 3, 4, 5])
        vector.setValues([])
        self.assertEqual(vector.getValues(), [])
        try:
            vector.setValues("a")
            assert False
        except:
            assert True

    def test_addScalar(self):
        vector = MyVector("abcd", "r", 1, [0, 0, 0, 0])
        vector.addScalar(2)
        self.assertEqual(vector.getValues(), [2, 2, 2, 2])
        vector.addScalar(-2)
        self.assertEqual(vector.getValues(), [0, 0, 0, 0])
        vector.addScalar(10)
        self.assertEqual(vector.getValues(), [10, 10, 10, 10])

    def test_addVector(self):
        vector = MyVector("abcd", "r", 1, [0, 0, 0, 0])
        vector.addVector([1, 2, 3, 4, 5, 6])
        self.assertEqual(vector.getValues(), [1, 2, 3, 4])
        vector.setValues([1, 2, 3, 4, 5, 6])
        vector.addVector([1, 2, 3])
        self.assertEqual(vector.getValues(), [2, 4, 6, 4, 5, 6])

    def test_subVector(self):
        vector = MyVector("abcd", "r", 1, [1, 2, 3, 4])
        vector.subVector([2, 2, 2, 2, 2, 2])
        self.assertEqual(vector.getValues(), [-1, 0, 1, 2])
        vector.setValues([1, 2, 3, 4, 5, 6])
        vector.subVector([3, -2, 1])
        self.assertEqual(vector.getValues(), [-2, 4, 2, 4, 5, 6])

    def test_mulVector(self):
        vector = MyVector("abcd", "r", 1, [1, 2, 3, 4])
        vector.multVector([2, 2, 2, 2, 2, 2])
        self.assertEqual(vector.getValues(), [2, 4, 6, 8])
        vector.setValues([1, 2, 3, 4, 5, 6])
        vector.multVector([3, -2, 1])
        self.assertEqual(vector.getValues(), [3, -4, 3, 4, 5, 6])

    def test_sumOfElements(self):
        vector = MyVector("abcd", "r", 1, [1, 2, 3, 4])
        self.assertEqual(vector.sumOfElements(), 10)
        vector.setValues([1, 2, 3, 4, 5, 6])
        self.assertEqual(vector.sumOfElements(), 21)
        vector.setValues([3, -4, 3, 4, 5, 6])
        self.assertEqual(vector.sumOfElements(), 17)

    def test_averageOfElements(self):
        vector = MyVector("abcd", "r", 1, [1, 2, 3, 4])
        self.assertEqual(vector.averageOfElements(), 2.5)
        vector.setValues([1, 2, 3, 4, 5, 6])
        self.assertEqual(vector.averageOfElements(), 3.5)
        vector.setValues([3, -4, 3, 4, 5, 6])
        self.assertEqual(vector.averageOfElements(), 17/6)

    def test_productOfElements(self):
        vector = MyVector("abcd", "r", 1, [1, 2, 3, 4])
        self.assertEqual(vector.productOfElements(), 24)
        vector.setValues([-1, 2, 3, 4, 5, 6])
        self.assertEqual(vector.productOfElements(), -720)
        vector.setValues([3, -4, 3, 4, 5, 6])
        self.assertEqual(vector.productOfElements(), -4320)

    def test_minOfElements(self):
        vector = MyVector("abcd", "r", 1, [1, 2, 3, 4])
        self.assertEqual(vector.minOfElements(), 1)
        vector.setValues([-1, 2, 3, 4, 5, 6])
        self.assertEqual(vector.minOfElements(), -1)
        vector.setValues([3, -4, 3, 4, 5, 6])
        self.assertEqual(vector.minOfElements(), -4)

    def test_maxOfElements(self):
        vector = MyVector("abcd", "r", 1, [1, 2, 3, 4])
        self.assertEqual(vector.maxOfElements(), 4)
        vector.setValues([-1, 2, 3, 4, 5, 6])
        self.assertEqual(vector.maxOfElements(), 6)
        vector.setValues([3, -4, 3, 4, 6, 5])
        self.assertEqual(vector.maxOfElements(), 6)


if __name__ == "__main__":
    unittest.main()
