import unittest

from beecrowd1117 import nota_correta

class verificacao_notas(unittest.TestCase):
    def test_verificacao(self):
        self.assertEqual(nota_correta(8,9),8.5)
        self.assertEqual(nota_correta(8,7),7.5)
        self.assertEqual(nota_correta(5.8,9.5),7.65)
        self.assertEqual(nota_correta(3,2),2.5)
        self.assertEqual(nota_correta(8,-1),"Uma das notas está errada")
        
if __name__ == '__main__':
    unittest.main()
