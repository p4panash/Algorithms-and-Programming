import unittest
from datetime import date
from Domain.Patients import Patients

class TestPatients(unittest.TestCase):

    def test_getAge(self):
        patient = Patients("Catalin", "Muntean", "1970716115195", "none")
