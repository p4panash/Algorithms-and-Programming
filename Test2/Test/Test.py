from Domain import Plant
from Infastructure import PlantRepository
import unittest

class TestPlant(unittest):
    def testGetPrice(self):
        plant = Plant("abc", 1, 10)
