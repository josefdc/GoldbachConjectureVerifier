import unittest
from verifier import es_primo, genera_lista_primos, descomponer_en_primos, verifica_goldbach_hasta

class TestGoldbachConjecture(unittest.TestCase):

    def test_es_primo(self):
        self.assertFalse(es_primo(0))
        self.assertFalse(es_primo(1))
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertFalse(es_primo(4))
        self.assertTrue(es_primo(5))
        self.assertFalse(es_primo(15))
        self.assertTrue(es_primo(17))

    def test_genera_lista_primos(self):
        self.assertEqual(genera_lista_primos(5), [2, 3, 5])
        self.assertEqual(genera_lista_primos(10), [2, 3, 5, 7])

    def test_descomponer_en_primos(self):
        primos_hasta_10 = genera_lista_primos(10)
        self.assertEqual(descomponer_en_primos(10, primos_hasta_10), (3, 7))
        self.assertEqual(descomponer_en_primos(8, primos_hasta_10), (3, 5))
        self.assertIsNone(descomponer_en_primos(3, primos_hasta_10))

    def test_verifica_goldbach_hasta(self):
        resultados = verifica_goldbach_hasta(10)
        self.assertEqual(resultados[4], (2, 2))
        self.assertEqual(resultados[6], (3, 3))
        self.assertEqual(resultados[8], (3, 5))
        self.assertEqual(resultados[10], (3, 7))

if __name__ == "__main__":
    unittest.main()
