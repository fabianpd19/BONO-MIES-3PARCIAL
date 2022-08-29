'''
Archivo python que ayudará a validar cada uno de los datos ingresados
en el método getDatos() del archivo main_bono
'''

import re
from tkinter import messagebox
from logicaNegocios import *

conectarMongo = PageLoader(myClient)

def validarNombresRE (value, campo):
    '''
    Valida cadenas, tales como nombres y apellidos de un usuario, es decir busca 
    que en una cadena solo existan caracteres alfabeticos de la a-z tanto 
    minúsculas como mayúsculas
    '''
    if re.search ('[a-zA-Z]', value):
        return True
    else: messagebox.showwarning("Error", f"{value} no es un {campo} válido.")

def validarCedulaRE (cedula):
    '''
    Valida que las cédulas contengan entre los primeros dos digitos de 
    01 - 25 (las cuales son cédulas del ecuador), y que también solo tengan
    10 dígitos
    '''
    if cedula in conectarMongo.queryCedulas():
        messagebox.showwarning("Error", "Está cédula ya fue ingresada")
    else:
        if re.search ("^[0-1][0-9]\d{8}$", cedula) or re.search ("^[2][0-5]\d{8}$", cedula):
            return True
        else: 
            messagebox.showwarning("Error", f"{cedula} no es una cédula válida.")

def validarCorreoRE(correo):
    '''
    Valida los correos que contengan un domino cualquiera de correo electrónico
    es decir, cualquier cadena que contenga @[cadena].[io-com-etc] será validado.
    '''
    if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', correo):
        return True
    else:
        messagebox.showwarning("Error", f"{correo} no es un correo válido.")

def validarEdadRE(edad):
    '''
    Valida que la edad sea un número y que también sea manyor a 18
    y menor a 65, tal y como lo dicen las rubricas del Bono MIES
    '''
    if re.search ("[0-9]", edad) and (int(edad)>=18 and int(edad)<=65):
        return True
    else:
        messagebox.showwarning("Error", f"{edad} no es una edad válida.")

def validarPyCRE(provincia, canton):
    '''
    Valida que existan datos en los campos de provincias y cantones en el registro de datos.
    '''
    if provincia in conectarMongo.mostrarProvincias() and canton in conectarMongo.cantones(provincia):
        return True
    else:
        messagebox.showwarning("Error", "Ingrese información en en el campo de Provincia o Cantón.")

def validarEstado(estado):
    '''
    Valida que exista un dato en el campo de estado
    '''
    if estado in conectarMongo.estadosUsuarios():
        return True
    else:
        messagebox.showwarning("Error", "Faltan campos en Estado.")

def validarRol(rol):
    '''
    Valida que exista un dato en el campo de rol
    '''
    if rol in conectarMongo.mostrarRoles():
        return True
    else:
        messagebox.showwarning("Error", "Falta campo en rol.")
