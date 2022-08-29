import unittest

from logicaNegocios import *
from main_bono import *

# class TestCedulas(unittest.TestCase):
#     '''
#     Clase la cual nos permite la validación de las cédulas dentro 
#     de nuestra base de datos.
#     ----
#     Atributos:
#     ....
#     ---------
#     test_verdadero_falso[1-7] (self):
#         Determina si existe o no la cédula de identidad de un usuario
#         en la base de datos.
#     '''

#     def test_verdadero_falso(self):
#         '''
#         Determina si existe o no la cédula de identidad de un usuario
#         en la base de datos.
#         '''
#         result = str_to_bool("2483845560")
#         self.assertTrue(result)

#     def test_verdadero_falso2(self):
#         '''
#         Determina si existe o no la cédula de identidad de un usuario
#         en la base de datos.
#         '''
#         result = str_to_bool("1128681001")
#         self.assertTrue(result)

#     def test_verdadero_falso3(self):
#         '''
#         Determina si existe o no la cédula de identidad de un usuario
#         en la base de datos.
#         '''
#         result = str_to_bool("1456757450")
#         self.assertTrue(result)

#     def test_verdadero_falso4(self):
#         '''
#         Determina si existe o no la cédula de identidad de un usuario
#         en la base de datos.
#         '''
#         result = str_to_bool("0256523516")
#         self.assertTrue(result)

#     def test_verdadero_falso5(self):
#         result = str_to_bool("0298151549")
#         self.assertTrue(result)

#     def test_verdadero_falso6(self):
#         result = str_to_bool("0894631681")
#         self.assertTrue(result)

#     def test_verdadero_falso7(self):
#         result = str_to_bool("2300284342")
#         self.assertTrue(result)

class TestCedulasRegex (unittest.TestCase):

    def test_itsCedula_ec (self):
        result = is_cedulaec_bool("1243512489124")
        self.assertTrue(result)

    def test_itsCedula_ec1 (self):
        result = is_cedulaec_bool("asjf123asa")
        self.assertTrue(result)

    def test_itsCedula_ec2 (self):
        result = is_cedulaec_bool("0325114724")
        self.assertTrue(result)

    def test_itsCedula_ec3 (self):
        result = is_cedulaec_bool("2207887027")
        self.assertTrue(result)

    def test_itsCedula_ec4 (self):
        result = is_cedulaec_bool("2207887027")
        self.assertTrue(result)

    def test_itsCedula_ec5 (self):
        result = is_cedulaec_bool("2627583012")
        self.assertTrue(result)

    def test_itsCedula_ec6 (self):
            result = is_cedulaec_bool("0376696972")
            self.assertTrue(result)

    def test_itsCedula_ec7 (self):
            result = is_cedulaec_bool("nombo1238428")
            self.assertTrue(result)


def str_to_bool(value):
    cedulasTotal=conectarMongo.queryCedulas()
    
    if value in cedulasTotal:
        return True
    if value in cedulasTotal:
        return False

def is_cedulaec_bool(value):

    if re.search ("^[0-1][0-9]\d{8}$", value) or re.search ("^[2][0-5]\d{8}$", value):
        return True
    else:
        return False      


if __name__ == '__main__':
    conectarMongo = PageLoader(myClient)
    unittest.main()