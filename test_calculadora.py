

import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(0, 0), 0)
        with self.assertRaises(ValueError):
            sumar(-1, 2)
        with self.assertRaises(ValueError):
            sumar("a", 2)

    def test_resta(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(2, 2), 0)
        with self.assertRaises(ValueError):
            restar(-1, 2)
        with self.assertRaises(ValueError):
            restar("a", 2)

    def test_multiplicacion(self):
        self.assertEqual(multiplicar(3, 2), 6)
        with self.assertRaises(ValueError):
            multiplicar(-1, 2)
        with self.assertRaises(ValueError):
            multiplicar("a", 2)

    def test_division(self):
        self.assertEqual(dividir(6, 2),3 )
        with self.assertRaises(ValueError):
            dividir(-1, 2)
        with self.assertRaises(ValueError):
            dividir(1, 0)
        with self.assertRaises(ValueError):
            dividir("a", 2)

if __name__ == '__main__':
    unittest.main()

