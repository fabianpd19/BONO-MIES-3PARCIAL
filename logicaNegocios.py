import pymongo

'''Conectar nuestro programa a MongoDb para la base de datos a utilizar.'''
#Conectar python a mongodb
myClient = pymongo.MongoClient("mongodb://localhost:27017/")
#Colecciones de MongoDB

MONGO_BASED = "bono-mies-data"
COLECCION_PERSONAS = "personas_bono_mies"
COLECCION_PYC = "provincias_cantones"
COLECCTION_ROLES = "roles_bono_mies"

# baseDatos = myClient[MONGO_BASED]
# coleccion = baseDatos [COLECCION]
# coleccionPyC = baseDatos [COLECCION2]

#Imagenes de fondo que se visualizan en cada ventana de tkinter
logginFondo = "fondo_main.png"
'''Fondo de la primera ventana'''

ingresarInfoFondo = "fondo_add_info.png" 
'''Fondo de la ventana de ingresar información'''

datosUsuarioFondo = "fondo_datos_user.png" 
'''Fondo de la ventana 'mostrar información' del usuario'''

adminFondo = "fondo_admin.png"
'''Fondo de la ventana principal'''

logoBono = "BONO.png"
'''Logo del bono mies'''


class DbConnectionMeta(type):
    '''
    Clase DbConnectionMeta
    ---
    Atributos
    ---------
    ...
    
    Métodos
    ---------
    __instancecheck__(self, instance):
        Se encarga de obtener la instancia de los objetos

    def __subclasscheck__(self, subclass):
        Retonar cada uno de los métodos a utilzar en la clase
    '''
    def __instancecheck__(self, instance):
        '''
        Se encarga de obtener la instancia de los objetos
        '''
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        '''
        Retonar cada uno de los métodos a utilzar en la clase
        '''
        return (hasattr(subclass, 'connect') and callable(subclass.connect))

class DbConnectionInterface(metaclass=DbConnectionMeta):
    '''
    Subclase DbConnectionInterface de DbConnectionMeta
    '''
    pass

class MyDBConection(DbConnectionInterface):
    '''
    Subclase MyDBConection de DbConnectionInterface
    '''
    def connect(self): 
        pass

class PageLoader():
    '''
    SubClase MyDBConection de DbConnectionInterface, permite conectarnos a una base de datos
    ---
    Atributos
    ---------
    db_connection: str
        Cadena que nos permite conocer el link para viincular nuestro código a nuestra base de datos
    
    Métodos
    ---------
    def __init__(self, db_connection: DbConnectionInterface):
        Constructor de cada uno de los atributos de la clase
    queryCedulas(self):
        Método encargado de recopilar todas las cédulas en una lista.
    mostrarProvincias(self):
        Recopila todas las provincias que se encuentra en la base de datos en una lista.
    

    '''
    def __init__(self, db_connection: DbConnectionInterface):
        '''
        Constructor de los parámetros
        ---
        Parámetros:
        ------
           db_connection: str
             Cadena que nos permite conocer el link para vincular nuestro código a nuestra base de datos
        '''
        #Asignación de las variables para conectar a la base de datos y acceder a las colecciones de la misma
        self._db_connection = db_connection
        self.baseDatos = self._db_connection[MONGO_BASED]
        self.coleccionPersonas = self.baseDatos[COLECCION_PERSONAS]
        self.coleccionPyC = self.baseDatos[COLECCION_PYC]
        self.coleccionRoles = self.baseDatos [COLECCTION_ROLES]

    def queryCedulas(self):
        '''
        Crear un array para poder verificar si existen estos datos en mongodb
        ---
        Return:
        --------
            return coleccionCedulas
                Retorna todas las cédulas que existen en la base de datos en forma de array
        '''
        coleccionTotal=self.coleccionPersonas.find()
        coleccionCedulas=[]
        for busqueda in coleccionTotal:
            coleccionCedulas.append(busqueda['cedula'])
        return coleccionCedulas
    
    def mostrarProvincias(self):
        '''
        Creación de array de la colección de provincias, que solo contengan provincias
        ---
        Return:
        --------
            return coleccionProvincia
                Retorna todas las provincias que existen en la base de datos en forma de array
        '''
        coleccionTotal=self.coleccionPyC.find()
        coleccionProvincia=[]
        for busqueda in coleccionTotal:
            coleccionProvincia.append(busqueda['provincia'])
        return coleccionProvincia

    def mostrarRoles(self):
        '''
        Creación de array con los roles de los usuarios de la base de datos
        ----
        Return:
        --------
            return coleccionRoles
                Retorna todos los roles que existen en la base de datos en forma de array
        '''
        coleccionTotal=self.coleccionRoles.distinct("rol")
        coleccionRoles=[]
        for busqueda in coleccionTotal:
            coleccionRoles.append(busqueda)
        return coleccionRoles

    def diccionarioPyC (self):
        '''
        Creación de array de la colección de provincias de la base de datos
        ----
        Return:
        --------
            return self.diccionario
                Retorna todas las provincias y cantones de la base de datos en un diccionario
        '''
        coleccionTotal=self.coleccionPyC.find()
        self.diccionario = {}
        for busqueda in coleccionTotal:
            provincia = busqueda["provincia"]
            self.diccionario [provincia] = self.cantones(provincia)
        return self.diccionario

    def cantones(self, provincia):
        '''
        Obtiene un array de los cantones de una provinca pasada por parametros
        ---
        Parámetros
        --------
        provincia: str
            Permite imprimir los cantones de la provincia pasada por parámetros
        ----
        Return:
        --------
            return self.array
                Retornar un array con los cantones de una provincia de la base de datos
        '''
        query = {"provincia": provincia}
        specificFind = self.coleccionPyC.find(query)
        self.array= []
        for find in specificFind:
            self.array = (find["cantones"])
        return self.array

    def listaGeneros(self):
        '''
        Creación de array de la colección de lista de generos
        ----
        Return:
        --------
            return self.coleccionGeneros
                Retornar un array con los generos de la base de datos
        '''
        coleccionTotal=self.coleccionPersonas.distinct("genero")
        self.coleccionGeneros=[]
        for busqueda in coleccionTotal:
            self.coleccionGeneros.append(busqueda)
        return self.coleccionGeneros

    def estadosUsuarios(self):
        '''
        Creación de array de la colección de los estados de los usuarios
        ----
        Return:
        --------
            return self.colecctioEstado
                Retornar un array con los estados de la base de datos
        '''
        coleccionTotal = self.coleccionPersonas.distinct("estado")
        self.colecctioEstado=[]
        for busqueda in coleccionTotal:
            self.colecctioEstado.append(busqueda)
        return self.colecctioEstado

    def beneficariosUsuarios(self):
        '''
        Creación de array de la colección de los estados de los usuarios
        ----
        Return:
        --------
            return self.colecctioEstado
                Retornar un array con los estados de la base de datos
        '''
        coleccionTotal = self.coleccionPersonas.distinct("beneficiario")
        self.colecctioEstado=[]
        for busqueda in coleccionTotal:
            self.colecctioEstado.append(busqueda)
        return self.colecctioEstado