import pymongo

'''Conectar nuestro programa a MongoDb para la base de datos a utilizar.'''
myClient = pymongo.MongoClient("mongodb://localhost:27017/")
MONGO_BASED = "bono-mies-data"
COLECCION = "personas_bono_mies"
baseDatos=myClient[MONGO_BASED]
coleccion = baseDatos [COLECCION]
coleccion.drop()

n = 30

for i in range (n):
    cedula = input(f"{i} Cedula\n")
    apellido = input (f"{i} Apellido\n")
    apellido2 = input (f"{i} Apellido2\n")
    nombre = input (f"{i} Nombre\n")
    nombre2 = input (f"{i} Nombre2\n")
    provincia = input (f"{i} Provincia\n")
    canton = input (f"{i} Ciudad\n")
    genero = input(f"{i} Genero\n")
    edad = input(f"{i} Edad\n")
    enter = input(f"{i}-{i}-{i}-{i}-{i}-{i}-{i}")
    datosDic={'nombre': nombre.upper(), 'nombre2': nombre2.upper(), 'apellido': apellido.upper(), 'apellido2':apellido2.upper(), 'canton': canton.upper(), 'provincia': provincia.upper(), 'cedula': cedula, 'edad': edad, 'genero':genero.upper()}
    updateDic=coleccion.insert_one(datosDic)
    print("-----")


# for i in range (n):
#     provincia = input(f"{i} Cedula\n")
#     apellido = input (f"{i} Apellido\n")
#     apellido2 = input (f"{i} Apellido2\n")
#     nombre = input (f"{i} Nombre\n")
#     nombre2 = input (f"{i} Nombre2\n")
#     provincia = input (f"{i} Provincia\n")
#     canton = input (f"{i} Ciudad\n")
#     genero = input(f"{i} Genero\n")
#     edad = input(f"{i} Edad\n")
#     enter = input(f"{i}-{i}-{i}-{i}-{i}-{i}-{i}")
#     #datosDic={'nombre': nombre.upper(), 'nombre2': nombre2.upper(), 'apellido': apellido.upper(), 'apellido2':apellido2.upper(), 'canton': canton.upper(), 'provincia': provincia.upper(), 'cedula': cedula, 'edad': edad, 'genero':genero.upper()}
#     #updateDic=coleccion.insert_one(datosDic)
#     print("-----")