import tkinter as tk
import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from feriados import *
from logicaNegocios import *

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
    
    def validar(self, cedula, message):
        '''
        Devolver true si está o false si no está el dato a buscar en la base de datos
        '''
        cedulasTotal=queryCedulas()
        if cedula in cedulasTotal:
            usuario.cedula=cedula
            datosUsuarioBono()
        else:
            messagebox.showwarning("Error", message)

    def validacionCedula (self):
        '''Retornar verdadero si la cédula es correspendiente a 10 dígitos, de lo contrario retorna falso'''
        return len(self.cedula) == 10

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

def logginCedula():
    mensaje = "Cédula incorrecta o no registrada."
    '''Inicializaición de la ventana'''
    ventana = tk.Tk()
    ventana.title("Validación de Cédula")
    '''Ajustar tamaño y definir que no se pueda cambiar el mismo'''
    ventana.geometry("600x600")
    ventana.resizable(width="False", height="False")
    '''Asignación de fondo'''
    img = tkinter.PhotoImage(file = logginFondo)
    lbl_imagen = tkinter.Label(ventana, image = img )
    lbl_imagen.pack()
    '''Entrada de texto'''
    entradaCedula=tk.Entry(ventana, font=font.Font(family="Arial", size = "10"),textvar="", width=32, relief="flat")
    entradaCedula.place(x=150, y=292)
    '''Mostrar texto'''
    mostrarTexto=tk.Label(ventana, text = "Ingrese su cédula de identidad")
    mostrarTexto.config(bg= "white", font=font.Font(family="Arial", size = "10"))
    mostrarTexto.place(x=190, y=253)
    '''Mostrar botón'''
    validarInfoB= tk.Button(ventana, text= "🔎", cursor="hand2", bg= "#0a509f",fg= "white",  width=2, height=1, relief="flat", command = lambda: usuario.validar(entradaCedula.get(), mensaje) ) 
    validarInfoB.place(x=432, y=286)
    registroInfo= tk.Button(ventana, text= "Regístrate", cursor="hand2", bg= "#0a509f",fg= "white",  width=7, height=1, relief="flat", command = validarFecha) 
    registroInfo.place(x=150, y=332)
    ventana.mainloop()

def agregarInfoMongoVentana():
    '''Recopilar información de los usuarios que se vayan a registrar por primera vez'''
    '''Inicializaición de la ventana'''
    ventana = Toplevel()
    ventana.title("Registro de información")
    '''Ajustar tamaño y definir que no se pueda cambiar el mismo'''
    ventana.geometry("600x600")
    ventana.resizable(width="False", height="False")
    '''Fondo de la primera parte del programa'''
    imagenFondo = tkinter.PhotoImage(file = ingresarInfoFondo)
    imagenFondoLabel = tkinter.Label(ventana, image = imagenFondo )
    imagenFondoLabel.pack()
    '''Labels en ventana'''
    '''Texto nombre'''
    mostrarLabel=tk.Label(ventana, text = "Nombre: ")
    mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
    mostrarLabel.place(x=95, y=125)
    '''Texto segundo nombre'''
    mostrarLabel=tk.Label(ventana, text = "Segundo Nombre: ")
    mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
    mostrarLabel.place(x=40, y=165)
    '''Texto apellido'''
    mostrarLabel=tk.Label(ventana, text = "Apellido: ")
    mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
    mostrarLabel.place(x=95, y=205)
    '''Texto segundo apellido'''
    mostrarLabel=tk.Label(ventana, text = "Segundo Apellido: ")
    mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
    mostrarLabel.place(x=40, y=245)
    '''Texto género'''
    mostrarLabel=tk.Label(ventana, text = "Género: ")
    mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
    mostrarLabel.place(x=400, y=125)
    '''Texto cédula'''
    mostrarLabel=tk.Label(ventana, text = "Cédula de Identidad: ")
    mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
    mostrarLabel.place(x=25, y=285)
    '''Texto provincia'''
    mostrarLabel=tk.Label(ventana, text = "Provincia: ")
    mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
    mostrarLabel.place(x=90, y=325)
    '''Texto Cantón'''
    mostrarLabel=tk.Label(ventana, text = "Cantón: ")
    mostrarLabel.config(bg= "#fafafb", fg="#4779b2",font=("Arial", 10, "bold"))
    mostrarLabel.place(x=105, y=365)
    '''Texto edad'''
    mostrarLabel=tk.Label(ventana, text = "Edad: ")
    mostrarLabel.config(bg= "#f4f4f4", fg="#4779b2",font=("Arial", 10, "bold"))
    mostrarLabel.place(x=115, y=405)
    '''Entradas de texto (Entrys)'''
    '''Entrada de texto del primer nombre'''
    nombreEntry=tk.Entry(ventana, font=font.Font(family="Arial", size = "10"),textvar="", width=25, relief="flat")
    nombreEntry.place(x=180, y=125)
    '''Entrada de texto del segundo nombre'''
    nombre2Entry = tk.Entry(ventana, font=font.Font(family="Arial", size = "10"),textvar="", width=25, relief="flat")
    nombre2Entry.place(x=180, y=165)
    '''Entrada de texto del primer apellido'''
    apellidoEntry = tk.Entry(ventana, font=font.Font(family="Arial", size = "10"),textvar="", width=25, relief="flat")
    apellidoEntry.place(x=180, y=205)
    '''Entrada de texto del segundo apellido'''
    apellido2Entry = tk.Entry(ventana, font=font.Font(family="Arial", size = "10"),textvar="", width=25, relief="flat")
    apellido2Entry.place(x=180, y=245)
    '''Entrada de texto de la ciudad del usuario'''
    cedulaEntry = tk.Entry(ventana, font=font.Font(family="Arial", size = "10"),textvar="", width=25, relief="flat")
    cedulaEntry.place(x=180, y=285)
    '''Menu despegable para elegir la provincia y el cantón del usuario'''
    provinciaEntry = ttk.Combobox(ventana, value= listaProvincias(), width=20, state="readonly")
    provinciaEntry.place(x=175, y=325)
    
    '''Botón'''
    getProvincia= tk.Button(ventana, text= "Actualizar", cursor="hand2", bg= "#0a509f",fg= "white",  width=10, height=1, relief="flat", command = lambda: getCanton(ventana, provinciaEntry.get())) 
    getProvincia.place(x=330, y=325)

    '''Entrada de texto de la edad del usuario'''
    edadEntry= tk.Entry(ventana, font=font.Font(family="Arial", size = "10"),textvar="", width=25, relief="flat")
    edadEntry.place(x=180, y=408)
    '''Lista con los generos dentro del menú despegable'''
    generoEntry = ttk.Combobox(ventana, value= listaGeneros(), width=10, state="readonly")
    generoEntry.place(x=460, y=125)
        
    '''Botón que registra los datos ingresados'''
    getDatosBoton= tk.Button(ventana, text= "Ingresar Datos", cursor="hand2", bg= "#0a509f",fg= "white",  width=10, height=1, relief="flat", command = lambda :  getDatos(nombreEntry.get(), nombre2Entry.get(), apellidoEntry.get(), apellido2Entry.get(), getCanton(ventana, provinciaEntry.get()), provinciaEntry.get(), cedulaEntry.get(), edadEntry.get(), generoEntry.get())) 
    getDatosBoton.place(x=259, y=464)
    '''Función para que no se cierre nuestra ventana'''
    ventana.mainloop()

def datosUsuarioBono ():
    '''Inicializaición de la ventana'''
    ventana = Toplevel()
    ventana.title("Datos")
    '''Ajustar tamaño y definir que no se pueda cambiar el mismo'''
    ventana.resizable(width="False", height="False")
    ventana.geometry("600x600")
    #asignación del fondo
    img = tkinter.PhotoImage(file = datosUsuarioFondo)
    lbl_imagen = tkinter.Label(ventana, image = img )
    lbl_imagen.pack()
    texto1=tk.Label(ventana, text = "Datos del Usuario")
    texto1.config(bg= "white", fg="#4779b2",font=("Arial", 11, "bold"))
    texto1.place(x=1, y=100)
    '''Texto de nombres'''
    query={"cedula": usuario.cedula}
    find = coleccion.find
    specificFind = coleccion.find(query)
    for find in specificFind:
        '''Mostrar el número de cédula en la ventana'''
        cedulaLabel=tk.Label(ventana, text = "Cédula: ")
        cedulaLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        cedulaLabel.place(x=300, y=120)        
        cedula=tk.Label(ventana, text = (find["cedula"]))
        cedula.config(bg= "white", fg="#4779b2",font=("Arial", 10))
        cedula.place(x=353, y=120)
        '''Mostrar nombres en la ventana'''
        nombresLabel=tk.Label(ventana, text = "Nombres: ")
        nombresLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        nombresLabel.place(x=1, y=120)        
        nombres=tk.Label(ventana, text = (find["nombre"], find["nombre2"]))
        nombres.config(bg= "white", fg="#4779b2",font=("Arial", 10))
        nombres.place(x=70, y=120)
        '''Mostrar apellidos en la ventana'''
        apellidosLabel=tk.Label(ventana, text = "Apellidos: ")
        apellidosLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        apellidosLabel.place(x=1, y=140)        
        apellidos=tk.Label(ventana, text = (find["apellido"], find["apellido2"]))
        apellidos.config(bg= "white", fg="#4779b2",font=("Arial", 10))
        apellidos.place(x=70, y=140)
        '''Mostrar provincia en la ventana'''
        provinciaLabel=tk.Label(ventana, text = "Provincia: ")
        provinciaLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        provinciaLabel.place(x=1, y=160)        
        provincia=tk.Label(ventana, text = (find["provincia"]))
        provincia.config(bg= "white", fg="#4779b2",font=("Arial", 10))
        provincia.place(x=70, y=160)
        '''Mostrar cantón'''
        provinciaLabel=tk.Label(ventana, text = "Cantón: ")
        provinciaLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        provinciaLabel.place(x=1, y=180)        
        provincia=tk.Label(ventana, text = (find["canton"]))
        provincia.config(bg= "white", fg="#4779b2",font=("Arial", 10))
        provincia.place(x=55, y=180)
        
        '''Mostrar el número de cédula en la ventana'''
        edadlabel=tk.Label(ventana, text = "Edad: ")
        edadlabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        edadlabel.place(x=300, y=140)        
        edad=tk.Label(ventana, text = (find["edad"]))
        edad.config(bg= "white", fg="#4779b2",font=("Arial", 10))
        edad.place(x=340, y=140)
        '''Mostrar el número de cédula en la ventana'''
        aprobadoLabel=tk.Label(ventana, text = "Estado: ")
        aprobadoLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        aprobadoLabel.place(x=300, y=200)        
        aprobado=tk.Label(ventana, text = "[✔] Aprovado")
        aprobado.config(bg= "white", fg="green",font=("Arial", 10))
        aprobado.place(x=350, y=200)
    ventana.mainloop()

#Validación de datos
def validarFecha():
    '''Devolver la fecha del sistema, para poder validar los feriados de ecuador '''
    #año=(datetime.datetime.now().date().year)
    fecha = (datetime.datetime.now().strftime('%Y-%m-%d'))
    #fecha = str(f"{año}{fecha}")
    online=False
    feriados=feriadosEcuador(fecha, online)
    if feriados.predict():
        messagebox.showwarning("Error", "El sistema de registro no se encuentra disponible.")
    else:
        agregarInfoMongoVentana()

def getDatos (nombre, nombre2, apellido, apellido2, canton, provincia, cedula, edad, genero):
    '''Validación de los datos'''
    '''Validar que no existan números en las cadenas a ingresar'''
    if validarDatos(nombre) == False:
        if validarDatos(nombre2) == False:
            if validarDatos(apellido) == False:
                if validarDatos(apellido2) == False:
                    usuario.cedula = cedula
                    '''Validar que la edad sea un número y comprobar que sea mayor de 18 años y menor a 100'''
                    if edad.isnumeric():
                        if int(edad)>=18 and int(edad)<=65:
                            '''Validar que la cédula contenga solo números y que sea igual a 10 digitos'''
                            if cedula.isnumeric():
                                if usuario.validacionCedula():
                                    '''Creación de un diccionario con los datos ingresados'''
                                    datosDic={'nombre': nombre.upper(), 'nombre2': nombre2.upper(), 'apellido': apellido.upper(), 'apellido2':apellido2.upper(), 'provincia': provincia.upper(), 'canton': canton.upper(), 'cedula': cedula.upper(), 'edad': edad.upper(), 'genero':genero.upper()}
                                    '''Agregamos nuetro diccionario a nuestra base de datos'''
                                    updateDic=coleccion.insert_one(datosDic)
                                    '''Mostrar mensaje de registro'''
                                else:
                                    messagebox.showwarning("Error", cedula + " no cédula no válida")
                            else:
                                messagebox.showwarning("Error", cedula + " no cédula no válida")
                        else:
                            messagebox.showwarning("Error", "La edad "+edad+" no es valida")
                    else:
                        messagebox.showwarning("Error", "La edad "+edad+" no es valida")

def validarDatos (datoValidar):
    '''Retornar verdadero si existen números en las cadenas y falso si no'''
    if (any(chr.isdigit() for chr in datoValidar)):
        messagebox.showwarning("Ingreso Incorrecto", datoValidar + " no es un dato válido")
    return (any(chr.isdigit() for chr in datoValidar))

#Listas de datos de MongoDB
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

def queryCedulas():
    '''Crear un array para poder verificar si existen estos datos en mongodb'''
    coleccionTotal=coleccion.find()
    coleccionCedulas=[]
    for busqueda in coleccionTotal:
        coleccionCedulas.append(busqueda['cedula'])
    return coleccionCedulas

def listaGeneros():
    '''Creación de array de la colección de provincias, que solo contengan provincias'''
    coleccionTotal=coleccion.distinct("genero")
    coleccionGeneros=[]
    for busqueda in coleccionTotal:
        coleccionGeneros.append(busqueda)
    return coleccionGeneros

def getCanton(ventana, provincia):    
    '''Función para actualizar la combobox secundaria de los cantones'''
    cantonEntry = ttk.Combobox(ventana, value= listaCantones(provincia), width=20, state="readonly")
    cantonEntry.place(x=175, y=365)
    return cantonEntry.get()

if __name__ == '__main__':

    '''Instancia de cada uno de las personas del bono-mies'''
    usuario=personaMies("","","", "", "", "", "", "", "", "", "", "", "")
    usuarioDiscapacidad=personaDiscapacidad("","","", "", "", "", "", "", "", "", "", "", "", "")
    usuasriBajosRecursos=personaBajosRecursos("","","", "", "", "", "", "", "", "", "", "", "")

    logginCedula()
    