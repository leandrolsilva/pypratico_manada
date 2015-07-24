import unittest
from unittest.case import TestCase

import os 
import sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import manada

#class TestManada(TestCase):
    #def test_manada(self):
        #m = Manada()
        #self.assertTrue(m)

class TestAnimals(TestCase):
    def test_animais(self):
        from manada.animais import Animal
        a = Animal()
        with self.assertRaises(NotImplementedError):
            a.barulho()

if __name__ == "__main__":
    unittest.main()
