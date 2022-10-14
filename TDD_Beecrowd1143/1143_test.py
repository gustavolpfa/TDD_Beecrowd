import unittest

from beecrowd1143 import valido

class verificacao_notas(unittest.TestCase):
    def verificacao(self):

        self.assertEqual(valido(200),'Invalido')
        self.assertEqual(valido(50),'Valido')
        self.assertEqual(valido(-15),'Invalido')
        self.assertEqual(valido(1),'Valido')
        
if __name__ == '__main__':
    unittest.main()
