import unittest
from unittest.case import TestCase

from os import path
import sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import manada

#class TestManada(TestCase):
    #def test_manada(self):
        #m = Manada()
        #self.assertTrue(m)

class TestAnimals(TestCase):
    from manada import animals
    from animals import Animal
    
    def test_animals(self):
        a = Animal()
        self.assertRaises(NotImplementedError, a.barulho())

if __name__ == "__main__":
    unittest.main()
