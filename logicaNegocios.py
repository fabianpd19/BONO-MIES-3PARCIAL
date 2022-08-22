import pymongo

'''Conectar nuestro programa a MongoDb para la base de datos a utilizar.'''
#Conectar python a mongodb
myClient = pymongo.MongoClient("mongodb://localhost:27017/")
#Colecciones de MongoDB
MONGO_BASED = "bono-mies-data"
COLECCION = "personas_bono_mies"
COLECCION2 = "provincias_cantones"

baseDatos = myClient[MONGO_BASED]
coleccion = baseDatos [COLECCION]
coleccionPyC = baseDatos [COLECCION2]

#Imagenes de fondo que se visualizan en cada ventana de tkinter
logginFondo = "fondo_main.png"
'''fondo de la primera ventana'''

ingresarInfoFondo = "fondo_add_info.png" 
'''fondo de la ventana de ingresar información'''

datosUsuarioFondo = "fondo_datos_user.png" 
'''fondo de la ventana 'mostrar información' del usuario'''