import unittest
from unittest.case import TestCase
from unittest.mock import Mock, PropertyMock

from os import path
import sys
lib_path = path.abspath(path.join('..'))
sys.path.append(lib_path)

#class TestManada(TestCase):
    #def test_manada(self):
        #m = Manada()
        #self.assertTrue(m)

class TestAnimais(TestCase):
    def setUp(self):
        import manada
        from manada.animais import Animal, Bicho
        self.Animal = Animal
        self.Bicho = Bicho

    def test_animais(self):
        with self.assertRaises(TypeError):
            a = self.Animal()

    def test_animais_not_implemented(self):
        a = self.Animal('animal','-')
        with self.assertRaises(NotImplementedError):
            a.barulho()

    def test_bicho_typeerror(self):
        with self.assertRaises(TypeError):
            c = self.Bicho()

    def test_bicho_ok(self):
        som = 'Au'
        animal = 'Cachorro'
        c = self.Bicho(animal, som)
        self.assertEqual(som, c.barulho())

class TestManada(TestCase):
    def setUp(self):
        import manada
        from manada.animais import Bicho
        self.m = manada.Manada()
        self.Bicho = Bicho

    def test_adicionar_animal(self):
        animal = 'Cachorro'
        som = 'Au'
        m = self.m
        bicho = self.Bicho(animal, som)
        m.adicionar_animal(bicho)
        self.assertIs(bicho, m.animal(animal))
        

if __name__ == "__main__":
    unittest.main()
