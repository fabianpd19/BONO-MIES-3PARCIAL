import tkinter as tk
import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from feriados import *
from logicaNegocios import *
from regular_expressions_validations import *

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
    estado: str
        Estado en el cual se encuentra el usuario en la base de datos del Bono mies
    rol:
        Rol con el que cumple el usuario
    correoElectronico: str
        Correo electrónico del usuario
    hijos: str
        Hijos que puede tener el usuario

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
            provincia: str
                Provincia de la ciudad de donde proviene el usuario
            canton: str
                canton de donde proviene el usuario
            cedula: str
                Cedula de identidad del usuario
            edad: str
                Edad del usuario
            genero: str
                Genero del usuario
            estado: str
                Estado en el cual se encuentra el usuario en la base de datos del Bono mies
            rol:
                Rol con el que cumple el usuario
            correoElectronico: str
                Correo electrónico del usuario
            hijos: str
                Hijos que puede tener el usuario
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

class personaMies (persona):
    '''
    Subclase de la clase persona, dentro de esta podremos determinar
    cada uno de los atributos a implementar en el sistema del BONO-MIES
    ---
    Atributos
    ----- 
    (Herda todos de la clase padre persona)
    Métodos
    -------
    def nombre (self):
        Obtiene el valor de el nombre
    def nombre (self, nombre):
        Establece el valor de el nombre
    def nombre2 (self):
        Obtiene el valor de el nombre2
    def nombre2 (self, nombre2):
        Establece el valor de el nombre2
    def apellido (self):
        Obtiene el valor de el apellido
    def apellido (self, apellido):
        Establece el valor de el apellido
    def apellido2 (self):
        Obtiene el valor de el apellido2
    def apellido2 (self, apellido2):
        Establece el valor de el apellido
    def provincia (self):
        Obtiene el valor de la provincia
    def provincia (self, provincia):
        Establece el valor de la provincia
    def canton (self):
        Obtiene el valor de el canton
    def canton (self, canton):
        Establece el valor de el canton
    def cedula (self):
        Obtiene el valor de la cédula
    def cedula (self, cedula):
        Establece el valor de la cédula
    def edad (self):
        Obtiene el valor de la edad
    def edad (self, edad):
        Establece el valor de la edad
    def genero (self):
        Obtiene el valor de el genero
    def genero (self, genero):
        Establece el valor de el genero
    def estado (self):
        Obtiene el valor de el estado
    def estado (self, estado):
        Establece el valor de el estado
    def rol (self):
        Obtiene el valor de el rol
    def rol (self, rol):
        Establece el valor de el rol
    def correoElectronico (self):
        Obtiene el valor de el correo electronico
    def correoElectronico (self, correoElectronico):
        Establece el valor de el correo electronico
    def hijos (self):
        Obtiene el valor de los hijos
    def hijos (self, hijos):
        Establece el valor de los hijos
    
    '''
    @property
    def nombre (self):
        '''Obtiene el valor de el nombre'''
        return self._nombre

    @nombre.setter
    def nombre (self, nombre):
        '''Establece el valor de el nombre'''
        self._nombre = nombre

    @property
    def nombre2 (self):
        '''Obtiene el valor de el nombre2'''
        return self._nombre2

    @nombre.setter
    def nombre2 (self, nombre2):
        '''Establece el valor de el nombre2'''
        self._nombre2 = nombre2

    @property
    def apellido (self):
        '''Obtiene el valor de el apellido'''
        return self._apellido

    @apellido.setter
    def apellido (self, apellido):
        '''Establece el valor de el apellido'''
        self._apellido = apellido   

    @property
    def apellido2 (self):
        '''Obtiene el valor de el apellido2'''
        return self._apellido2

    @apellido2.setter
    def apellido2 (self, apellido2):
        '''Establece el valor de el apellido'''
        self._apellido2 = apellido2 

    @property
    def provincia (self):
        '''Obtiene el valor de la provincia'''
        return self._provincia

    @provincia.setter
    def provincia (self, provincia):
        '''Establece el valor de la provincia'''
        self._provincia = provincia

    @property
    def canton (self):
        '''Obtiene el valor de el canton'''
        return self._provincia

    @canton.setter
    def canton (self, canton):
        '''Establece el valor de el canton'''
        self._canton = canton

    @property
    def cedula (self):
        '''Obtiene el valor de la cédula'''
        return self._cedula

    @cedula.setter
    def cedula (self, cedula):
        '''Establece el valor de la cédula'''
        self._cedula = cedula

    @property
    def edad (self):
        '''Obtiene el valor de la edad'''
        return self._edad

    @edad.setter
    def edad (self, edad):
        '''Establece el valor de la edad'''
        self._edad = edad

    @property
    def genero (self):
        '''Obtiene el valor de el genero'''
        return self._genero

    @genero.setter
    def genero (self, genero):
        '''Establece el valor de el genero'''
        self._genero = genero

    @property
    def estado (self):
        '''Obtiene el valor de el estado'''
        return self._estado

    @estado.setter
    def estado (self, estado):
        '''Establece el valor de el estado'''
        self._estado = estado

    @property
    def rol (self):
        '''Obtiene el valor de el rol'''
        return self._rol

    @rol.setter
    def rol (self, rol):
        '''Establece el valor de el rol'''
        self._rol = rol

    @property
    def correoElectronico (self):
        '''Obtiene el valor de el correo electronico'''
        return self._correoElectronico

    @correoElectronico.setter
    def correoElectronico (self, correoElectronico):
        '''Establece el valor de el correo electronico'''
        self._correoElectronico = correoElectronico

    @property
    def hijos (self):
        '''Obtiene el valor de los hijos'''
        return self._hijos

    @hijos.setter
    def hijos (self, hijos):
        '''Establece el valor de los hijos'''
        self._hijos = hijos

class ventanaTkinter():
    '''
    Subclase ventana, se encarga de configurar la ventana
    y agregar widgets para que estos sean mostrados en la interfaz gráfica.
    ---
    Atributos
    -------
    ventana = tk
        Ventana a configurar (Heredado de la clase ventanaTkinter)
    Métodos:
    ----------
    __init__(self, ventana):
        Cosntructor de los atributos de la clase
    '''
    def __init__(self, ventana):
    
        '''
        Constructor de los parámetros a usar
        ---
        Parámetros:
            ventana: str
                Variable donde se asignará la ventana la cual se va a mostrar
        '''
        self.ventana = ventana
    
class ventanasMies (ventanaTkinter):
    '''
    Subclase ventana, se encarga de configurar la ventana
    y agregar widgets para que estos sean mostrados en la interfaz gráfica.
    ---
    Atributos
    -------
    ventana = tk
        Ventana a configurar (Heredado de la clase ventanaTkinter)
    Métodos:
    ----------
    ventanasMies (self):
        Permite la configuración directa de la ventana.
    widgetsValidar (self):
        Mostrar por pantalla los widgets que se van a utilizar en la ventana principal
    '''

    def ventanasMies (self):
        '''
        Configuración de la ventana principal (validación de la cédula de identidad)
        '''
        #Asignación de un ícono a la ventana
        self.ventana.tk.call('wm', 'iconphoto', self.ventana._w, tk.PhotoImage(file='icono.png'))
        #Títutlo a la ventana
        self.ventana.title("BONO - MIES")
        #Color de fondo de la ventana
        self.ventana.config(bg="white")
        #Tamaño de la ventana
        self.ventana.geometry("600x600")
        #No poder modificar el tamaño de la ventana
        self.ventana.resizable(width="False", height="False")
        
        #Asignación de un fondo al programa
        self.img = tkinter.PhotoImage(file = logginFondo)
        Label(self.ventana, image = self.img ).pack()

        '''Entrada de texto de la cédula de identidad del usuario'''
        self.entradaCedula=tk.Entry(self.ventana, font=font.Font(family="Arial", size = "10"),textvar="", width=32, relief="flat")
        self.entradaCedula.place(x=150, y=292)

        '''Llamada a los widgets de validación'''
        self.widgetsValidar()

    def widgetsValidar (self):
        '''
        Creación de cada uno los widgets a mostrar en la ventana de validación de la cédula
        '''
        mostrarTexto=tk.Label(self.ventana, text = "Ingrese su cédula de identidad")
        mostrarTexto.config(bg= "white", font=font.Font(family="Arial", size = "10"))
        mostrarTexto.place(x=190, y=253)      
        validarInfoB= tk.Button(self.ventana, 
            text= "🔎", 
            cursor="hand2", 
            bg= "#0a509f",
            fg= "white",  
            width=2, 
            height=1, 
            relief="flat", 
            command = lambda : (validarCedula(self.entradaCedula.get()))) 
        validarInfoB.place(x=432, y=286)
        registroInfo= tk.Button(self.ventana, 
            text= "Regístrate", 
            cursor="hand2", 
            bg= "#0a509f",
            fg= "white",  
            width=7, 
            height=1, 
            relief="flat", 
            command = (validarFecha)) 
        registroInfo.place(x=150, y=332)   
    
    def ventanaRegistro(self):
        '''
        Definición de la ventana la cual se va a hacer uso para el ingreso de datos de los usuarios
        '''
        #Cierre de la ventana anterior
        self.ventana.withdraw()
        #Asinación de una subventana
        self.ventanaAgregarInfo=tk.Toplevel()
        
        '''Propiedades de la ventana'''
        self.ventanaAgregarInfo.title("Registro de información")
        self.ventanaAgregarInfo.geometry("600x600")
        self.ventanaAgregarInfo.resizable(width="False", height="False")

        self.img = tkinter.PhotoImage(file = ingresarInfoFondo)
        Label(self.ventanaAgregarInfo, image = self.img ).pack()
        
    def ventanaRegistroW(self):
        self.ventanaRegistro()
        self.widgetsVentanaRegistro()
    
    def widgetsVentanaRegistro(self):
        '''
        Creación de cada uno los widgets a mostrar en la ventana de validación de la cédula
        '''

        '''Label texto primer nombre'''
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Nombre: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=95, y=125)
        '''Label texto segundo nombre'''
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Segundo Nombre: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=40, y=165)
        '''Label texto apellido'''
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Apellido: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=95, y=205)
        '''Label texto segundo apellido'''
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Segundo Apellido: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=40, y=245)
        '''Label texto género'''
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Género: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=360, y=125)
        '''Label texto cédula'''
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Cédula de Identidad: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=25, y=285)
        '''Label texto provincia'''
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Provincia: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=90, y=325)
        '''Label texto Cantón'''
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Cantón: ")
        mostrarLabel.config(bg= "#fafafb", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=105, y=365)
        '''Label texto edad'''
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Edad: ")
        mostrarLabel.config(bg= "#f4f4f4", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=115, y=405)
        '''Label correo electrónico'''
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Correo Electrónico: ")
        mostrarLabel.config(bg= "#EEEDEE", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=35, y=455)
        '''Label texto Hijos del usuario'''
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Hijos: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=370, y=165)
        '''Label texto estados en los que puede estar un usuario'''
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Estado: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=365, y=205)

        '''Entradas de texto (Entrys)'''
        '''Entrada de texto del primer nombre'''
        self.nombreEntry=tk.Entry(self.ventanaAgregarInfo, font=font.Font(family="Arial", size = "10"),textvar="", width=15, relief="flat")
        self.nombreEntry.place(x=180, y=125)
        '''Entrada de texto del segundo nombre'''
        self.nombre2Entry = tk.Entry(self.ventanaAgregarInfo, font=font.Font(family="Arial", size = "10"),textvar="", width=15, relief="flat")
        self.nombre2Entry.place(x=180, y=165)
        '''Entrada de texto del primer apellido'''
        self.apellidoEntry = tk.Entry(self.ventanaAgregarInfo, font=font.Font(family="Arial", size = "10"),textvar="", width=15, relief="flat")
        self.apellidoEntry.place(x=180, y=205)
        '''Entrada de texto del segundo apellido'''
        self.apellido2Entry = tk.Entry(self.ventanaAgregarInfo, font=font.Font(family="Arial", size = "10"),textvar="", width=15, relief="flat")
        self.apellido2Entry.place(x=180, y=245)
        '''Entrada de texto de la ciudad del usuario'''
        self.cedulaEntry = tk.Entry(self.ventanaAgregarInfo, font=font.Font(family="Arial", size = "10"),textvar="", width=15, relief="flat")
        self.cedulaEntry.place(x=180, y=285)
        '''Entrada de texto de la edad del usuario'''
        self.edadEntry= tk.Entry(self.ventanaAgregarInfo, font=font.Font(family="Arial", size = "10"),textvar="", width=15, relief="flat")
        self.edadEntry.place(x=180, y=408)
        '''Entrada de texto del correo electrónico del usuario'''
        self.correoElectronico= tk.Entry(self.ventanaAgregarInfo, font=font.Font(family="Arial", size = "10"),textvar="", width=15, relief="flat")
        self.correoElectronico.place(x=180, y=457)
        '''Entrada de texto de la cantidad de hijos del usuario'''
        self.hijosEntry= tk.Entry(self.ventanaAgregarInfo, font=font.Font(family="Arial", size = "10"),textvar="", width=15, relief="flat")
        self.hijosEntry.place(x=425, y=165)


        #COMBOBOXS
        '''Menu despegable para elegir la provincia y el cantón del usuario'''
        self.provinciaEntry = ttk.Combobox(
            self.ventanaAgregarInfo, 
            width=20, 
            state="readonly",
            values=tuple(conectarMongo.diccionarioPyC().keys()))
        self.provinciaEntry.place(x=175, y=325)
        self.provinciaEntry.bind("<<ComboboxSelected>>", on_combobox_select)

        '''Menu despegable cantón que dependerá de las opciones de la ventana provincia'''
        self.cantonEntry = ttk.Combobox(self.ventanaAgregarInfo, width=20, state="readonly")
        self.cantonEntry.place(x=175, y=365)

        '''Menú despegable donde mostrará la lista de generos a las que se puede elegir'''
        self.generoEntry = ttk.Combobox(self.ventanaAgregarInfo, value= conectarMongo.listaGeneros(), width=10, state="readonly")
        self.generoEntry.place(x=425, y=125)

        '''Menú despegable donde mostrará la lista de estados a las que se puede elegir'''
        self.estadoEntry = ttk.Combobox(self.ventanaAgregarInfo, value= conectarMongo.estadosUsuarios(), width=15, state="readonly")
        self.estadoEntry.place(x=425, y=205)

        self.estado = "USUARIO"
        #botones
        getDatosBoton= tk.Button(self.ventanaAgregarInfo, text= "Ingresar Datos", 
            cursor="hand2", bg= "#0a509f",fg= "white",  
            width=10, height=1, relief="flat", 
            command = (self.ingresarInformacion))
        getDatosBoton.place(x=400, y=464)

    def ingresarInformacion(self):
        if(bool(getDatos(
                self.nombreEntry.get(),
                self.nombre2Entry.get(),
                self.apellidoEntry.get(),
                self.apellido2Entry.get(),
                self.provinciaEntry.get(),
                self.cantonEntry.get(),
                self.cedulaEntry.get(),
                self.edadEntry.get(),
                self.generoEntry.get(),
                self.estadoEntry.get(),
                self.correoElectronico.get(),
                self.hijosEntry.get(),
                self.estado
            ))):
            messagebox.showinfo("Datos Ingresados", "¡Datos ingresados correctamente!")
        

    def mostrarInformacion(self):
        '''
        El procedimiento mostrarInformacion se encarga de mostrar toda
        la información de un usuario, esto por medio al cédula que ya fue 
        validad anteriormente.
        '''
        
        #Cerramos la ventana principal
        self.ventana.withdraw()

        #Inicializamos la ventana de mostrarInformación
        self.ventanaMostrarInf = tk.Toplevel()
        self.ventanaMostrarInf.title("Datos")
        self.ventanaMostrarInf.geometry("600x600")
        self.ventanaMostrarInf.resizable(width="False", height="False")

        #Asignación de una imagen como fondo a la ventana
        self.img = tkinter.PhotoImage(file = datosUsuarioFondo)
        Label(self.ventanaMostrarInf, image = self.img ).pack()
        
        '''Label Datos Usuarios'''
        texto1=tk.Label(self.ventanaMostrarInf, text = "Datos del Usuario")
        texto1.config(bg= "white", fg="#4779b2",font=("Arial", 11, "bold"))
        texto1.place(x=1, y=100)

        '''Texto de nombres'''
        query={"cedula": personaMies.cedula} 
        '''Query que nos va a permitir mostrar la información que contiene la cédula ingresada'''
        find = conectarMongo.coleccionPersonas.find()
        specificFind = conectarMongo.coleccionPersonas.find(query)
        for find in specificFind:
            '''Mostrar información del usuario ingresado.'''

            '''Mostar cédula del usuario en la ventana'''
            cedulaLabel=tk.Label(self.ventanaMostrarInf, text = "Cédula: ")
            cedulaLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
            cedulaLabel.place(x=300, y=120)        
            cedula=tk.Label(self.ventanaMostrarInf, text = (find["cedula"]))
            cedula.config(bg= "white", fg="#4779b2",font=("Arial", 10))
            cedula.place(x=353, y=120)
            
            '''Mostrar nombres en la ventana'''
            nombresLabel=tk.Label(self.ventanaMostrarInf, text = "Nombres: ")
            nombresLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
            nombresLabel.place(x=1, y=120)        
            nombres=tk.Label(self.ventanaMostrarInf, text = (find["nombre"], find["nombre2"]))
            nombres.config(bg= "white", fg="#4779b2",font=("Arial", 10))
            nombres.place(x=70, y=120)
            
            '''Mostrar apellidos en la ventana'''
            apellidosLabel=tk.Label(self.ventanaMostrarInf, text = "Apellidos: ")
            apellidosLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
            apellidosLabel.place(x=1, y=140)        
            apellidos=tk.Label(self.ventanaMostrarInf, text = (find["apellido"], find["apellido2"]))
            apellidos.config(bg= "white", fg="#4779b2",font=("Arial", 10))
            apellidos.place(x=70, y=140)
            
            '''Mostrar provincia en la ventana'''
            provinciaLabel=tk.Label(self.ventanaMostrarInf, text = "Provincia: ")
            provinciaLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
            provinciaLabel.place(x=1, y=160)        
            provincia=tk.Label(self.ventanaMostrarInf, text = (find["provincia"]))
            provincia.config(bg= "white", fg="#4779b2",font=("Arial", 10))
            provincia.place(x=70, y=160)
            
            '''Mostrar cantón'''
            provinciaLabel=tk.Label(self.ventanaMostrarInf, text = "Cantón: ")
            provinciaLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
            provinciaLabel.place(x=1, y=180)        
            provincia=tk.Label(self.ventanaMostrarInf, text = (find["canton"]))
            provincia.config(bg= "white", fg="#4779b2",font=("Arial", 10))
            provincia.place(x=55, y=180)
            
            '''Mostrar el número de cédula en la ventana'''
            edadlabel=tk.Label(self.ventanaMostrarInf, text = "Edad: ")
            edadlabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
            edadlabel.place(x=310, y=140)        
            edad=tk.Label(self.ventanaMostrarInf, text = (find["edad"]))
            edad.config(bg= "white", fg="#4779b2",font=("Arial", 10))
            edad.place(x=350, y=140)

            '''Mostrar el número de cédula en la ventana'''
            edadlabel=tk.Label(self.ventanaMostrarInf, text = "Correo: ")
            edadlabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
            edadlabel.place(x=300, y=160)        
            edad=tk.Label(self.ventanaMostrarInf, text = (find["correoElectronico"]))
            edad.config(bg= "white", fg="#4779b2",font=("Arial", 10))
            edad.place(x=350, y=160)

            '''Mostrar el género del usuario en la ventana'''
            edadlabel=tk.Label(self.ventanaMostrarInf, text = "Genero: ")
            edadlabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
            edadlabel.place(x=1, y=200)        
            edad=tk.Label(self.ventanaMostrarInf, text = (find["genero"]))
            edad.config(bg= "white", fg="#4779b2",font=("Arial", 10))
            edad.place(x=55, y=200)

            if int(find["hijos"]) > 0:
                '''Mostrar el género del usuario en la ventana'''
                edadlabel=tk.Label(self.ventanaMostrarInf, text = "Hijos: ")
                edadlabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
                edadlabel.place(x=1, y=220)        
                edad=tk.Label(self.ventanaMostrarInf, text = (find["hijos"]))
                edad.config(bg= "white", fg="#4779b2",font=("Arial", 10))
                edad.place(x=40, y=220)

            '''Mostrar si el usuario es beneficiario o no en la ventana'''
            aprobadoLabel=tk.Label(self.ventanaMostrarInf, text = "Beneficiario: ")
            aprobadoLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
            aprobadoLabel.place(x=290, y=200)

            if (find["beneficiario"] == "SI"):     
                '''
                Si el usuario es beneficiario, se mostrará por pantalla que lo es
                caso contrario se mostrá que no está denegado
                '''   
                aprobado=tk.Label(self.ventanaMostrarInf, text = "[✔] Aprovado")
                aprobado.config(bg= "white", fg="green",font=("Arial", 10))

            elif(find["beneficiario"]=="NO"):
                aprobado=tk.Label(self.ventanaMostrarInf, text = "[❌] Denegado")
                aprobado.config(bg= "white", fg="red",font=("Arial", 10))

            elif(find["beneficiario"]=="EN PROCESO"):
                aprobado=tk.Label(self.ventanaMostrarInf, text = "[⌛] En proceso")
                aprobado.config(bg= "white", fg="gray",font=("Arial", 10))
            aprobado.place(x=380, y=200)

class ventanaMiesAdmin(ventanaTkinter):
    '''
    Subclase ventanaMiesAdmin, se encarga de configurar la ventana
    y agregar widgets para que estos sean mostrados en la interfaz gráfica.
    ---
    Atributos
    -------
    ventana = tk
        Ventana a configurar (Heredado de la ventana ventanaTkinter)
    Métodos:
    ----------
    ventanaControl (self):
        Permite la configuración directa de la ventana administrador.
    '''

    def ventanaControl (self):
        '''
        Configuración de la ventana principal del CRUD
        '''
        #Se cierra la ventana anterior
        self.ventana.withdraw()
        #Asignamos una subventana
        self.ventanaCRUD = tk.Toplevel()

        '''Propiedades de la ventana'''
        self.ventanaCRUD.title("BONO - MIES")
        self.ventanaCRUD.config(bg="white")
        self.ventanaCRUD.geometry("1040x500")
        self.ventanaCRUD.resizable(width="False", height="False")

        self.tablaDatos()

    def tablaDatos (self):
        '''
        Función donde se encuentran widgets, entre los principales
        destaca el TreeView para la recopilación de información en una tabla
        '''
        scrollbarX = Scrollbar (self.ventanaCRUD, orient = HORIZONTAL)
        scrollbarY = Scrollbar (self.ventanaCRUD, orient = VERTICAL)
        
        #Asignación de columbas de la tabla
        self.tablaDatos = ttk.Treeview(self.ventanaCRUD, columns =  ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12'))
        
        #Propiedades de la tabla (posición y tamaño)
        self.tablaDatos.place(relx=0.00, rely=0.200, width=1020, height=380)

        #Creación de scrollbars, tanto en eje vertica como en eje horizontal 
        scrollbarX.place(relx= 0, rely =0.965, width=1020)
        scrollbarY.place(relx= 0.98, rely =0.0, height=500)
        
        #Configuración de las scrollbars para sincronizarlas con la tabla
        self.tablaDatos.configure(xscrollcommand=scrollbarX.set, yscrollcommand=scrollbarY.set)
        scrollbarY.configure(command=self.tablaDatos.yview)
        scrollbarX.configure(command=self.tablaDatos.xview)

        #Asignación de propiedades a cada una de las columnas de la tabla
        self.tablaDatos.heading("#0", text = "Cédula",anchor=W)
        self.tablaDatos.heading("#1", text = "Nombre",anchor=W)
        self.tablaDatos.heading("#2", text = "Nombre2",anchor=W)
        self.tablaDatos.heading("#3", text = "Apellido",anchor=W)
        self.tablaDatos.heading("#4", text = "Apellido2",anchor=W)
        self.tablaDatos.heading("#5", text = "Provincia",anchor=W)
        self.tablaDatos.heading("#6", text = "Cantón",anchor=W)
        self.tablaDatos.heading("#7", text = "Genero",anchor=W)
        self.tablaDatos.heading("#8", text = "Estado",anchor=W)
        self.tablaDatos.heading("#9", text = "Rol",anchor=W)
        self.tablaDatos.heading("#10", text = "CorreoElectronico",anchor=W)
        self.tablaDatos.heading("#11", text = "Hijos",anchor=W)
        self.tablaDatos.heading("#12", text = "Beneficiario",anchor=W)

        #Llamado de funciones para la tabla
        self.insertDatesTable()
        self.widgetsCRUD()

    def widgetsCRUD(self):
        '''
        Creación de cada uno los widgets para ingresar datos a la base de datos.
        '''

        '''Label texto primer nombre'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Nombre: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=0, y=1)
        '''Label texto segundo nombre'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Nombre 2: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=0, y=25)
        '''Label texto apellido'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Apellido: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=0, y=50)
        '''Label texto segundo apellido'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Apellido 2: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=0, y=75)
        '''Label texto género'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Género: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=200, y=1)
        '''Label texto cédula'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Cédula: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=200, y=25)
        '''Label texto provincia'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Provincia: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=189, y=50)
        '''Label texto Cantón'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Cantón: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=200, y=75)
        '''Label texto edad'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Edad: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=350, y=1)
        '''Label correo electrónico'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Correo: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=350, y=25)
        '''Label texto Hijos del usuario'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Hijos: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=350, y=75)
        '''Label texto estados en los que puede estar un usuario'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Estado: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=350, y=50)
        '''Label texto roles de los usuarios existentes'''
        mostrarLabel=tk.Label(self.ventanaCRUD, text = "Rol: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=530, y=75)

        '''Entradas de texto (Entrys)'''
        '''Entrada de texto del primer nombre'''
        self.nombreEntry=tk.Entry(self.ventanaCRUD, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.nombreEntry.place(x=65, y=0)
        '''Entrada de texto del segundo nombre'''
        self.nombre2Entry = tk.Entry(self.ventanaCRUD, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.nombre2Entry.place(x=65, y=25)
        '''Entrada de texto del primer apellido'''
        self.apellidoEntry = tk.Entry(self.ventanaCRUD, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.apellidoEntry.place(x=65, y=50)
        '''Entrada de texto del segundo apellido'''
        self.apellido2Entry = tk.Entry(self.ventanaCRUD, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.apellido2Entry.place(x=65, y=75)
        '''Entrada de texto de la ciudad del usuario'''
        self.cedulaEntry = tk.Entry(self.ventanaCRUD, font=font.Font(family="Arial", size = "8"),textvar="", width=13, relief="solid")
        self.cedulaEntry.place(x=250, y=25)
        '''Entrada de texto de la edad del usuario'''
        self.edadEntry= tk.Entry(self.ventanaCRUD, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.edadEntry.place(x=400, y=1)
        '''Entrada de texto del correo electrónico del usuario'''
        self.correoElectronico= tk.Entry(self.ventanaCRUD, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.correoElectronico.place(x=400, y=25)
        '''Entrada de texto de la cantidad de hijos del usuario'''
        self.hijosEntry= tk.Entry(self.ventanaCRUD, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.hijosEntry.place(x=400, y=75)

        #COMBOBOXS
        '''Menu despegable para elegir la provincia y el cantón del usuario'''
        self.provinciaEntry = ttk.Combobox(
            self.ventanaCRUD, 
            width=10, 
            state="readonly",
            values=tuple(conectarMongo.diccionarioPyC().keys()))
        self.provinciaEntry.place(x=250, y=50)
        self.provinciaEntry.bind("<<ComboboxSelected>>", on_combobox_select1)

        '''Menu despegable cantón que dependerá de las opciones de la ventana provincia'''
        self.cantonEntry = ttk.Combobox(self.ventanaCRUD, width=10, state="readonly")
        self.cantonEntry.place(x=250, y=75)

        '''Menú despegable donde mostrará la lista de generos a las que se puede elegir'''
        self.generoEntry = ttk.Combobox(self.ventanaCRUD, value= conectarMongo.listaGeneros(), width=8, state="readonly")
        self.generoEntry.place(x=250, y=1)

        '''Menú despegable donde mostrará la lista de estados a las que se puede elegir'''
        self.estadoEntry = ttk.Combobox(self.ventanaCRUD, value= conectarMongo.estadosUsuarios(), width=15, state="readonly")
        self.estadoEntry.place(x=400, y=50)

        '''Menú despegable donde mostrará la lista de roles a las que se puede elegir'''
        self.estadoEntry = ttk.Combobox(self.ventanaCRUD, value= conectarMongo.mostrarRoles(), width=15, state="readonly")
        self.estadoEntry.place(x=560, y=75)
        
        #BOTONES
        getDatosBoton= tk.Button(self.ventanaCRUD, text= "Ingresar Datos", 
            cursor="hand2", bg= "#0a509f",fg= "white",  
            width=10, height=1, relief="flat", 
            command = self.actualizarTabla)
        getDatosBoton.place(x=530, y=1)

        actualizarTabla= tk.Button(self.ventanaCRUD, text= "Actualizar", 
            cursor="hand2", bg= "#0A9F45",fg= "white",  
            width=10, height=1, relief="flat", command = self.insertDatesTable)

        actualizarTabla.place(x=530, y=30)

        editarTabla= tk.Button(self.ventanaCRUD, text= "Editar", 
            cursor="hand2", bg= "#0A9F8F",fg= "white",  
            width=10, height=1, relief="flat", command = self.obtenerDato)

        editarTabla.place(x=620, y=1)

        eliminarTabla= tk.Button(self.ventanaCRUD, text= "Eliminar", 
            cursor="hand2", bg= "#9F0A25",fg= "white",  
            width=10, height=1, relief="flat", command = self.elimarDato)

        eliminarTabla.place(x=620, y=30)
    
    def insertDatesTable(self):
        '''
        Función que permite ingresar datos a la tabla y mostrarla en la misma
        (Esta se actualizará cada que se llame a la misma)
        '''
        datos = self.tablaDatos.get_children()
        for dato in datos:
            self.tablaDatos.delete(dato)

        listaDatos = conectarMongo.coleccionPersonas.find()
        for listaDatos in conectarMongo.coleccionPersonas.find():
            self.tablaDatos.insert("", END, text = (listaDatos["cedula"]), values=(listaDatos["nombre"], 
            listaDatos["nombre2"],
            listaDatos["apellido"],
            listaDatos["apellido2"],
            listaDatos["provincia"],
            listaDatos["canton"],
            listaDatos["genero"],
            listaDatos["estado"],
            listaDatos["rol"],
            listaDatos["correoElectronico"],
            listaDatos["hijos"],
            listaDatos["beneficiario"]
            ))
    
    def actualizarTabla (self):
        getDatos(
                self.nombreEntry.get(),
                self.nombre2Entry.get(),
                self.apellidoEntry.get(),
                self.apellido2Entry.get(),
                self.provinciaEntry.get(),
                self.cantonEntry.get(),
                self.cedulaEntry.get(),
                self.edadEntry.get(),
                self.generoEntry.get(),
                self.estadoEntry.get(),
                self.correoElectronico.get(),
                self.hijosEntry.get(),
                self.estadoEntry.get()
            )
        self.insertDatesTable()
        
    def obtenerDato (self):
        selected_item = self.tablaDatos.focus()
        item_details = self.tablaDatos.item(selected_item)
        return item_details.get("text")

    def elimarDato (self):
        query = {"cedula": self.obtenerDato()}
        conectarMongo.coleccionPersonas.delete_one(query)
        self.insertDatesTable()

def validarCedula(cedula):
    '''
    Funcón encarga de validar que exista una cédula en la base de datos
    '''
    cedulasTotal=conectarMongo.queryCedulas()
    if cedula in cedulasTotal:
        '''
        Si la cédula se encuentra en la base de datos, validará
        el rango del usuario para determinar si es un usuario normal
        o un admistrador
        '''
        personaMies.cedula=cedula
        validarRango()
    else:
        messagebox.showwarning("Error", "Ingrese una cédula de identidad válida.")

def on_combobox_select(event):
    '''
    Función encargada de validar la información de un 
    combobox dependiente de otro por medio de un diccionario
    '''
    window.cantonEntry.set("")
    window.cantonEntry.config(values=conectarMongo.diccionarioPyC()[window.provinciaEntry.get()])
    pass

def on_combobox_select1(event):
    '''
    Función encargada de validar la información de un 
    combobox dependiente de otro por medio de un diccionario
    '''
    ventanaAdmin.cantonEntry.set("")
    ventanaAdmin.cantonEntry.config(values=conectarMongo.diccionarioPyC()[ventanaAdmin.provinciaEntry.get()])
    pass

def getDatos (nombre, nombre2, apellido, apellido2, provincia, canton, cedula, edad, genero, estado, correoElectronico, hijos, rol):
    '''
    Método el cual se encarga validar cada uno de los datos que ingresa un usuario:
    El ingreso de datos personales como nombres o apellidos serán validados que no tengan números
    '''
    if validarNombresRE(nombre, 'nombre'): #Validar nombre
        if validarNombresRE(nombre2, 'nombre'): #Validar nombre2
            if validarNombresRE(apellido, 'apellido'): #Validar apellido
                if validarNombresRE(apellido2, 'apellido'): #Validar apellido2
                    if validarCedulaRE(cedula): #Validar cédula
                        if validarPyCRE(provincia, canton): #Validar provincia y cantón
                                if validarEdadRE(edad): #Validar edad
                                        if validarCorreoRE(correoElectronico): #Validar correo electrónico
                                            if hijos.isnumeric(): #Validar edad
                                                if validarRol(rol):
                                                    '''
                                                    Siendo todos los datos validados se crea un diccionario
                                                    mismo el cual será ingresado en la base de datos.
                                                    '''
                                                    diccionario={'nombre': nombre.upper(), 
                                                                'nombre2':nombre2.upper(), 
                                                                'apellido': apellido.upper(), 
                                                                'apellido2': apellido2.upper(),
                                                                'provincia': provincia, 
                                                                'canton': canton, 
                                                                'cedula': cedula, 
                                                                'edad': edad,
                                                                'genero': genero,
                                                                'estado': estado,
                                                                'rol': rol,
                                                                'correoElectronico': correoElectronico,
                                                                'hijos': hijos,
                                                                'beneficiario' : "EN PROCESO"
                                                                }
                                                    #Ingresamos el diccionario a nuestra base de datos.
                                                    updateDataBase=conectarMongo.coleccionPersonas.insert_one(diccionario)
                                                    return True
                                                    
                                            else:
                                                messagebox.showwarning("Error", hijos + " no es un valor válido")
                                                
def validarRango():
    '''
    Función encargada de validar el rango de un usuario mediante 
    la cédula ingresada.
    '''
    query={"cedula": personaMies.cedula}
    find = conectarMongo.coleccionPersonas.find()
    specificFind = conectarMongo.coleccionPersonas.find(query) 
    for find in specificFind: #Busca el rango de la persona con respecto a la cédula ingresada
        if find["rol"] == "ADMIN":
            '''Si el usuario tiene rango admin lo mandará a la ventanda de administracion'''          
            ventanaAdmin.ventanaControl()
        else:
            '''Si el usuario tiene rango usuario será direccionaro a la ventana de mostrar información'''
            window.mostrarInformacion()

def validarFecha():
    '''
    Devolver la fecha del sistema, para poder validar los feriados de ecuador 
    '''
    fecha = (datetime.datetime.now().strftime('%Y-%m-%d'))
    online=False
    feriados=feriadosEcuador(fecha, online)
    '''
    Si la fecha es un día festivo no nos permitirá registar nueva información
    '''
    if feriados.predict():
        '''
        Si la fecha es un día festivo no nos permitirá registar nueva información
        '''
        messagebox.showwarning("Error", "El sistema de registro no se encuentra disponible.")
    else:
        '''En caso de que esté en una fecha laborable si podremos ingresar nueva información'''
        window.ventanaRegistroW()



if __name__ == '__main__':
    conectarMongo = PageLoader(myClient)
    '''Instancia de la clase a PageLoader para poder conectar a MongoDB'''

    '''Instancia de Tkinter tanto como de la clase ventanasMies para abrir la ventana principal'''    
    ventana = Tk()
    
    window = ventanasMies (ventana)
    ventanaAdmin=ventanaMiesAdmin(ventana)
    
    '''Llamamos a la ventana principal'''
    window.ventanasMies()
    #ventanaAdmin.ventanaControl()
    '''Instancia de la clase personaMies'''
    personaBono = personaMies("", "", "", "", "", "", "", "", "", "", "", "", "")

    '''Función mainloop'''
    ventana.mainloop()