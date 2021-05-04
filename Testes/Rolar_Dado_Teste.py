import unittest
from Controllers import Rolar_Dado


class MyTestCase(unittest.TestCase):

    def Deve_retornar_erro_quando_rolar_um_dado_de_zero_faces(self):
        self.assertEqual(Rolar_Dado.dado(0), 0)


if __name__ == '__main__':
    unittest.main()
