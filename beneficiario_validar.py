from logicaNegocios import *
from main_bono import *


def getDatos (nombre, nombre2, apellido, apellido2, provincia, canton, cedula, edad, genero, estado, correoElectronico, hijos):
    diccionario={'nombre': nombre, 
                'nombre2':nombre2, 
                'apellido': apellido, 
                'apellido2': apellido2,
                'provincia': provincia, 
                'canton': canton, 
                'cedula': cedula, 
                'edad': edad,
                'genero': genero,
                'estado': estado,
                'rol': 'USUARIO',
                'correoElectronico': correoElectronico,
                'hijos': hijos,
                'beneficiario' : "EN PROCESO"
                }