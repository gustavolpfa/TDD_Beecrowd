import unittest

from beecrowd1132 import soma_muts

class verificacao_notas(unittest.TestCase):
   def test_soma_multiplos(self):
        self.assertEqual(soma_muts(0, 0), 0)
        self.assertEqual(soma_muts(100, 101), 201)
        self.assertEqual(soma_muts(200, 87), 15072)
        self.assertEqual(soma_muts(-137, -243), -18822)
        self.assertEqual(soma_muts(-15, 0), -107)

        
if __name__ == '__main__':
    unittest.main()
