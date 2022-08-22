import unittest

from main_bono import *
from logicaNegocios import *

class TestCedulasPalma(unittest.TestCase):

    def test_verdadero_falso(self):
        result = str_to_bool("2412431594")
        self.assertTrue(result)

    def test_verdadero_falso2(self):
        result = str_to_bool("1746312830")
        self.assertTrue(result)

    def test_verdadero_falso3(self):
        result = str_to_bool("1343565583")
        self.assertTrue(result)

    def test_verdadero_falso4(self):
        result = str_to_bool("2042459881")
        self.assertTrue(result)

    def test_verdadero_falso5(self):
        result = str_to_bool("0643883225")
        self.assertTrue(result)

    def test_verdadero_falso6(self):
        result = str_to_bool("0326895198")
        self.assertTrue(result)

    def test_verdadero_falso7(self):
        result = str_to_bool("1032378805")
        self.assertTrue(result)


class TestCedulasCastellano(unittest.TestCase):

    def test_verdadero_falso(self):
        result = str_to_bool("2483845560")
        self.assertTrue(result)

    def test_verdadero_falso2(self):
        result = str_to_bool("1128681001")
        self.assertTrue(result)

    def test_verdadero_falso3(self):
        result = str_to_bool("1456757450")
        self.assertTrue(result)

    def test_verdadero_falso4(self):
        result = str_to_bool("0256523516")
        self.assertTrue(result)

    def test_verdadero_falso5(self):
        result = str_to_bool("0298151549")
        self.assertTrue(result)

    def test_verdadero_falso6(self):
        result = str_to_bool("0894631681")
        self.assertTrue(result)

    def test_verdadero_falso7(self):
        result = str_to_bool("2171955777")
        self.assertTrue(result)


def str_to_bool(value):

    if value in queryCedulas():
        return True
    if value in queryCedulas():
        return False        


if __name__ == '__main__':
    unittest.main()