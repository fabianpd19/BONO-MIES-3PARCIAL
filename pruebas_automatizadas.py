import unittest

from logicaNegocios import *
import re

class TestCedulas(unittest.TestCase):
    '''
    Clase la cual nos permite la validación de las cédulas dentro 
    de nuestra base de datos.
    ----
    Atributos: (Heredados de la clase padre)
    -----
    test_verdadero_falso[1-7] (self):
        Determina si existe o no la cédula de identidad de un usuario
        en la base de datos.
    '''
    def test_verdadero_falso(self):
        '''
        Determina si existe o no la cédula de identidad de un usuario
        en la base de datos.
        '''
        result = str_to_bool("2483845560")
        self.assertTrue(result)

    def test_verdadero_falso2(self):
        '''
        Determina si existe o no la cédula de identidad de un usuario
        en la base de datos.
        '''
        result = str_to_bool("1128681001")
        self.assertTrue(result)

    def test_verdadero_falso3(self):
        '''
        Determina si existe o no la cédula de identidad de un usuario
        en la base de datos.
        '''
        result = str_to_bool("1456757450")
        self.assertTrue(result)

    def test_verdadero_falso4(self):
        '''
        Determina si existe o no la cédula de identidad de un usuario
        en la base de datos.
        '''
        result = str_to_bool("0256523516")
        self.assertTrue(result)

    def test_verdadero_falso5(self):
        '''
        Determina si existe o no la cédula de identidad de un usuario
        en la base de datos.
        '''
        result = str_to_bool("0298151549")
        self.assertTrue(result)

    def test_verdadero_falso6(self):
        '''
        Determina si existe o no la cédula de identidad de un usuario
        en la base de datos.
        '''
        result = str_to_bool("0894631681")
        self.assertTrue(result)

    def test_verdadero_falso7(self):
        '''
        Determina si existe o no la cédula de identidad de un usuario
        en la base de datos.
        '''
        result = str_to_bool("2300284342")
        self.assertTrue(result)

class TestCedulasRegex (unittest.TestCase):
    '''
    Clase la cual nos permite la validación de las cédulas con respecto
    a si son de ecuador y contienen 10 digitos de longitud
    ----
    Atributos: (Heredados de la clase padre)
    -----
    test_itsCedula_ec[1-7] (self):
        Determina si la cédula ingresada es válida o no
    '''
    def test_itsCedula_ec (self):
        '''
        Determina si la cédula ingresada es válida o no
        '''
        result = is_cedulaec_bool("1243512489124")
        self.assertTrue(result)

    def test_itsCedula_ec1 (self):
        '''
        Determina si la cédula ingresada es válida o no
        '''
        result = is_cedulaec_bool("asjf123asa")
        self.assertTrue(result)

    def test_itsCedula_ec2 (self):
        '''
        Determina si la cédula ingresada es válida o no
        '''
        result = is_cedulaec_bool("0325114724")
        self.assertTrue(result)

    def test_itsCedula_ec3 (self):
        '''
        Determina si la cédula ingresada es válida o no
        '''
        result = is_cedulaec_bool("2207887027")
        self.assertTrue(result)

    def test_itsCedula_ec4 (self):
        '''
        Determina si la cédula ingresada es válida o no
        '''
        result = is_cedulaec_bool("2207887027")
        self.assertTrue(result)

    def test_itsCedula_ec5 (self):
        '''
        Determina si la cédula ingresada es válida o no
        '''
        result = is_cedulaec_bool("2627583012")
        self.assertTrue(result)

    def test_itsCedula_ec6 (self):
        '''
        Determina si la cédula ingresada es válida o no
        '''
        result = is_cedulaec_bool("0376696972")
        self.assertTrue(result)

    def test_itsCedula_ec7 (self):
        '''
        Determina si la cédula ingresada es válida o no
        '''
        result = is_cedulaec_bool("nombo1238428")
        self.assertTrue(result)

def str_to_bool(value):
    '''
    Permite saber si una cédula existe dentro de la base de datos
    Si existe retorna True, caso contrario retorna False
    '''
    cedulasTotal=conectarMongo.queryCedulas()
    
    if value in cedulasTotal:
        return True
    if value in cedulasTotal:
        return False

def is_cedulaec_bool(value):
    '''
    Permite saber si una cédula es válida haciendo uso de expresiones regulares:
    Si tiene digitos de una cédula ecuatoriana y si tiene 10 digitos de longitud
    '''
    if re.search ("^[0-1][0-9]\d{8}$", value) or re.search ("^[2][0-5]\d{8}$", value):
        return True
    else:
        return False      

if __name__ == '__main__':
    '''Instancia de la clase PageLoader para conectar a la base de datos'''
    conectarMongo = PageLoader(myClient)
    '''Llamamos a la función que nos permite correr las pruebas automatizadas'''
    unittest.main()