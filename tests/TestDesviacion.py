# tests/TestDesviacion.py
import unittest
from src.logica.Desviacion import Desviacion

class TestDesviacion(unittest.TestCase):
    

    def test_conjunto_vacio_retornaNone(self):
        d = Desviacion([])
        self.assertIsNone(d.calcular())

    
    def test_un_elemento_retornaCero(self):
        d = Desviacion([5])
        self.assertEqual(0, d.calcular())


    def test__dos__elementos(self):
        d = Desviacion([5,7])
        self.assertEqual(1, d.calcular())


    def test_n_elementos(self):
        d = Desviacion([2, 4, 8, 9, 10, 15])
        self.assertAlmostEqual(4.20, d.calcular(), places=2)