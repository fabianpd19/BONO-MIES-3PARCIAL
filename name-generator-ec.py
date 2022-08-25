import pymongo
import random
import random as r

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def nombres():
    n = 180

    for i in range (n):
        print(f"{i+1}-{i+1}-{i+1}-{i+1}-{i+1}-{i+1}-{i+1}")
        nombre = input (f"[{i+1}] NOMBRE\n-")
        datosDic={'nombre': nombre.upper()}
        updateDic=coleccionMujeres.insert_one(datosDic)

def apellidos():
    n = 300

    for i in range (n):
        print(f"{i+1}-{i+1}-{i+1}-{i+1}-{i+1}-{i+1}-{i+1}")
        apellido = input (f"[{i+1}] APELLIDO\n-")
        datosDic={'apellido': apellido.upper()}
        updateDic=coleccionApellidos.insert_one(datosDic)

def arrayHombres():
    '''Creación de array de la colección de provincias, que solo contengan provincias'''
    coleccionTotal=coleccionHombres.find()
    arrayNombres=[]
    for busqueda in coleccionTotal:
        arrayNombres.append(busqueda['nombre'])
    return arrayNombres

def arrayMujeres():
    '''Creación de array de la colección de provincias, que solo contengan provincias'''
    coleccionTotal=coleccionMujeres.find()
    arrayNombres=[]
    for busqueda in coleccionTotal:
        arrayNombres.append(busqueda['nombre'])
    return arrayNombres

def arrayApellidos():
    '''Creación de array de la colección de provincias, que solo contengan provincias'''
    coleccionTotal=coleccionApellidos.find()
    arrayNombres=[]
    for busqueda in coleccionTotal:
        arrayNombres.append(busqueda['apellido'])
    return arrayNombres

def generarDatosHombres():
    array = arrayHombres()
    numero = random.randint(0, 130)
    nombre = array [numero]
    return nombre

def generarDatosMujer():
    array = arrayMujeres()
    numero = random.randint(0, 179)
    nombre = array [numero]
    return nombre

def generarDatosApellidos():
    array = arrayApellidos()
    numero = random.randint(0, 299)
    apellido = array [numero]
    return apellido

def numeroTelefon():
    ph_no = []
    ph_no.append("09")
    for i in range(0, 8):
        ph_no.append(r.randint(0, 9))
    
    num = "".join(map(str, ph_no))
    
    return num

def generarCedula():
    listaCedula = [
        '01',
        '02',
        '03',
        '04',
        '05',
        '06',
        '07',
        '08',
        '09',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17',
        '18',
        '19',
        '20',
        '21',
        '22',
        '23',
        '24',
    ]

    numeroProvincia = r.randint(0, 23)
    cedula = []
    cedula.append(listaCedula[numeroProvincia])
    for i in range(0, 8):
        cedula.append(r.randint(0, 9))
    
    num = "".join(map(str, cedula))
    
    return num

def listaProvincias():
    '''Creación de array de la colección de provincias, que solo contengan provincias'''
    coleccionTotal=coleccionPyC.find()
    coleccionProvincia=[]
    for busqueda in coleccionTotal:
        coleccionProvincia.append(busqueda['provincia'])
    return coleccionProvincia

def listaCantones(provincia):
    '''Creación de array de la colección de provincias, que solo contengan provincias'''
    query = {"provincia": provincia}
    specificFind = coleccionPyC.find(query)
    array= []
    for find in specificFind:
        array = (find["cantones"])
    return array

def generarDatosProvincia():
    array = listaProvincias()
    numero = random.randint(0, 23)
    provincia = array [numero]
    return provincia

def generarDatosCanton(provincia):
    array = listaCantones(provincia)
    cantidadCanton = len(array)
    cantidadCanton = cantidadCanton - 1
    numero = random.randint(0, cantidadCanton)
    canton = array [numero]
    return canton

def correoElectronico (nombre, apellido, cedula):
    listaCorreos = [
        "@gmail.com",
        "@hotmail.com",
        "@outlook.com",
        "@yahoo.mail",
    ]
    a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
    
    trans = str.maketrans(a,b)
    
    nombre = nombre.translate(trans)
    apellido = apellido.translate(trans)

    dividir = len(nombre)
    dividir = dividir/2
    nombre = nombre[:int(dividir)]
    dividir = len(apellido)/2
    apellido = apellido[:int(dividir)]
    cedulaRandom = random.randint(1, 4)
    cedula = cedula [:cedulaRandom]
    correoRandom = random.randint(0, 3)
    correo = listaCorreos [correoRandom]

    return nombre.lower() + apellido.lower() + cedula + correo

if __name__ == "__main__":
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    MONGO_BASED = "nombres_apellidos" #bono-mies-data
    COLECCION = "nombres_hombres"
    COLECCION2 = "nombres_mujeres"
    COLECCION3 = "apellidos_total"

    baseDatos = myClient[MONGO_BASED]
    coleccionHombres = baseDatos [COLECCION]
    coleccionMujeres = baseDatos [COLECCION2]
    coleccionApellidos = baseDatos [COLECCION3]

    MONGO_MIES = "bono-mies-data"
    COLECCION_MIES = "personas_bono_mies"
    COLECCION2_MIES = "provincias_cantones"

    baseDatosMies = myClient[MONGO_MIES]
    coleccion = baseDatosMies [COLECCION_MIES]
    coleccionPyC = baseDatosMies [COLECCION2_MIES]
    #########################################

    listaHijos = [
        'NONE',
        'NONE',
        'NONE',
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        3,
        3,
        4,
        5,
        6,
    ]

veces = 5

genero = ["HOMBRE", "MUJER"]
estados = ["POBREZA EXTREMA", "NONE", "DISCAPACIDAD", "MADRE SOLTERA"]


for k in range (veces):
        print('\n')
        provincia = generarDatosProvincia()
        canton = generarDatosCanton(provincia)
        beneficario = 'NO'

        i = r.randint(0, 1)
        if i == 0:
            nombre = generarDatosHombres()
            nombre2 = generarDatosHombres()
            contador = r.randint(0, 2)
            hijos = random.randint(0, 14)
            if contador == 0 or contador == 2:
                beneficario = 'SI'

        else:
            nombre = generarDatosMujer()
            nombre2 = generarDatosMujer()
            contador = r.randint(0, 3)
            
            if contador == 3:
                hijos = random.randint(3, 14)
            else:
                hijos = random.randint(0, 14)
                beneficario = 'SI'

        apellido = generarDatosApellidos()
        apellido2 = generarDatosApellidos()
        cedula = generarCedula()
        edad = r.randint(18, 65)
        hijototal = listaHijos[hijos] 

        diccionario={'nombre': nombre, 
        'nombre2':nombre2, 
        'apellido': apellido, 
        'apellido2': apellido2,
        'provincia': provincia, 
        'canton': canton, 
        'cedula': cedula, 
        'edad': edad,
        'genero': genero[i],
        'estado': estados[contador],
        'rol': 'USUARIO',
        'correoElectronico': correoElectronico(nombre, apellido, cedula),
        'hijos': hijototal,
        'beneficiario' : beneficario
        }
        print (diccionario)
        # updateDic=coleccion.insert_one(diccionario)
        # print(f"{bcolors.OK} {k+1} File Saved Successfully!{bcolors.RESET}")

# diccionario={
# 'nombre': 'FABIAN', 
# 'nombre2':'ALEXANDER', 
# 'apellido': 'PALMA', 
# 'apellido2': 'DUEÑAS',
# 'provincia': 'SANTO DOMINGO', 
# 'canton': 'SANTO DOMINGO', 
# 'cedula': '2300284342', 
# 'edad': '19',
# 'genero': 'HOMBRE',
# 'estado': 'NONE',
# 'rol': 'ADMIN',
# 'correoElectronico': 'fabianapd12@gmail.com',
# 'hijos': 'NONE',
# 'beneficiario' : 'NO'
# }

# print (diccionario)
# updateDic=coleccion.insert_one(diccionario)
# print(f"{bcolors.OK} {1} File Saved Successfully!{bcolors.RESET}")


# print(coleccion.distinct("cedula"))

n = 4

# print("\nCEDULAS QUE NO EXISTEN")

# for i in range (n):
#     print(generarCedula())

    


class persona:
    def __init__(self, nombre, nombre2, apellido, apellido2, provincia, canton, cedula, edad, genero, estado, rol, correoElectronico, hijos):
        self.nombre = nombre
        self.nombre2 = nombre2
        self.apellido = apellido
        self.apellido2 = apellido2
        self.canton = canton
        self.provincia = provincia
        self.cedula = cedula
        self.edad = edad
        self.genero = genero
        self.estado = estado
        self.rol = rol
        self.correoElectronico = correoElectronico
        self.hijos = hijos
    
    @property
    def nombre (self):
        return self._nombre

    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre

    @property
    def nombre2 (self):
        return self._nombre2

    @nombre.setter
    def nombre2 (self, nombre2):
        self._nombre2 = nombre2

    @property
    def apellido (self):
        return self._apellido

    @apellido.setter
    def apellido (self, apellido):
        self._apellido = apellido   

    @property
    def apellido2 (self):
        return self._apellido2

    @apellido2.setter
    def apellido2 (self, apellido2):
        self._apellido2 = apellido2 

    @property
    def provincia (self):
        return self._provincia

    @provincia.setter
    def provincia (self, provincia):
        self._provincia = provincia

    @property
    def canton (self):
        return self._provincia

    @canton.setter
    def canton (self, canton):
        self._canton = canton   
        