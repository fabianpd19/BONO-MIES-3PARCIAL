class persona:
    '''
    Clase para poder determinar cada uno de los datos detalladamente de cada uno
    de los usuarios, para tener un control sobre cada uno los mismos y poder determinar sus 
    necesidades
    ---
    Atributos
    --------
    nombre: str
        Primer nombre del usuario
    nombre2: str
        Segundo nombre del usuario
    apellido: str
        Primer apellido del usuario
    apellido2: str
        Segundo apellido del usuario
    ciudad: str
        Ciudad de donde proviene el usuario
    provincia: str
        Provincia de la ciudad de donde proviene el usuario
    cedula: str
        Cedula de identidad del usuario
    edad: str
        Edad del usuario
    genero: str
        Genero del usuario
    Métodos
    -------
    __init__(self, nombre, nombre2, apellido, apellido2, ciudad, provincia, cedula, edad):
        Constructor de cada uno de los atributos de nuestra clase persona
    
    validar(self):
        Valida si la cédula de un usuario está dentro de la base de datos
    validacionCedula():
        Valida si la cédula del usuari es correspondiente a 10 digitos

    '''
    def __init__(self, nombre, nombre2, apellido, apellido2, provincia, canton, cedula, edad, genero, estado, rol, correoElectronico, hijos):
        '''
        Constructor de todos los elementos de la clase persona
        '''
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

class personaMies(persona):
    '''
    Clase para poder determinar cada uno de los datos detalladamente de cada uno
    de los usuarios, para tener un control sobre cada uno los mismos y poder determinar sus 
    necesidades
    ---
    Atributos
    --------
    Atributos (Todos los atributos son heredados de la clase principal persona)

    Métodos
    -------
    __init__(self, nombre, nombre2, apellido, apellido2, ciudad, provincia, cedula, edad):
        Constructor de cada uno de los atributos de nuestra clase persona
    
    validar(self):
        Valida si la cédula de un usuario está dentro de la base de datos
    validacionCedula():
        Valida si la cédula del usuari es correspondiente a 10 digitos

    '''
    pass

class personaDiscapacidad (persona):
    '''
    Subclase de la clase persona. 
    Clase para determinar las necesidades en específico de una persona con discapcidad
    y así calcular el bono a recibir
    ---
    Atributos (Todos los atributos son heredados de la clase principal persona)
    carnetConadis = str *atributo propio
        Carnet encargado de valir si la persona tiene discapacidad, y poder acceder así a más beneficios del bono 
    --------
    Métodos
    -------
    __init__(self, nombre, nombre2, apellido, apellido2, ciudad, provincia, cedula, edad):
        Constructor de cada uno de los atributos
    carnetDiscapcidad (self):
        Método para la respectiva verificación del carnet de discapacidad

    '''
    def __init__(self, nombre, nombre2, apellido, apellido2, canton, provincia, cedula, edad, genero, estado, rol, correoElectronico, hijos, carnetConadis):
        self.carnetConadis = carnetConadis
        super().__init__(nombre, nombre2, apellido, apellido2, canton, provincia, cedula, edad, genero, estado, rol, correoElectronico, hijos)
    def carnetDiscapcidad (self):
        '''Método para la creación del carnet de dispacadidad'''
        pass

class personaBajosRecursos (persona):
    '''
    Subclase de la clase persona. 
    Clase para determinar las necesidades en específico de una persona con discapcidad
    y así calcular el bono a recibir
    ---
    Atributos (Todos los atributos son heredados de la clase principal persona)
    --------
    Métodos
    --------
    '''
    pass