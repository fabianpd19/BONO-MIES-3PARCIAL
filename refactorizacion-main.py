from email import contentmanager
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

    @property
    def cedula (self):
        return self._cedula

    @cedula.setter
    def cedula (self, cedula):
        self._cedula = cedula

    @property
    def edad (self):
        return self._edad

    @edad.setter
    def edad (self, edad):
        self._edad = edad

    @property
    def genero (self):
        return self._genero

    @genero.setter
    def genero (self, genero):
        self._genero = genero

    @property
    def estado (self):
        return self._estado

    @estado.setter
    def estado (self, estado):
        self._estado = estado

    @property
    def rol (self):
        return self._rol

    @rol.setter
    def rol (self, rol):
        self._rol = rol

    @property
    def correoElectronico (self):
        return self._correoElectronico

    @correoElectronico.setter
    def correoElectronico (self, correoElectronico):
        self._correoElectronico = correoElectronico

    @property
    def hijos (self):
        return self._hijos

    @hijos.setter
    def hijos (self, hijos):
        self._hijos = hijos


    
   

class ventanasMies ():
    '''
    Clase ventana, se encarga de configurar la ventana
    y agregar widgets para que estos sean mostrados en la interfaz gráfica.
    ---
    Atributos
    -------
    ventana = tk
        Ventana a configurar
    Métodos:
    ----------
    __init__(self, ventana):
        Cosntructor de los atributos de la clase
    ventanasMies (self):
        Permite la configuración directa de la ventana.
    widgetsValidar (self):
        Mostrar por pantalla los widgets que se van a utilizar en la ventana principal

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

    def ventanasMies (self):
        '''
        Configuración de la ventana principal (validación de la cédula de identidad)
        '''
        self.ventana.tk.call('wm', 'iconphoto', self.ventana._w, tk.PhotoImage(file='icono.png'))
        self.ventana.title("BONO - MIES")
        self.ventana.config(bg="white")
        self.ventana.geometry("600x600")
        self.ventana.resizable(width="False", height="False")
        
        #Asignación de un fondo al programa
        self.img = tkinter.PhotoImage(file = logginFondo)
        Label(self.ventana, image = self.img ).pack()
        self.entradaCedula=tk.Entry(self.ventana, font=font.Font(family="Arial", size = "10"),textvar="", width=32, relief="flat")
        self.entradaCedula.place(x=150, y=292)
        ventanasMies.widgetsValidar(self)

    def widgetsValidar (self):
        '''
        Creación de cada uno los widgets a mostrar en la ventana de validación de la cédula
        '''
        mostrarTexto=tk.Label(self.ventana, text = "Ingrese su cédula de identidad")
        mostrarTexto.config(bg= "white", font=font.Font(family="Arial", size = "10"))
        mostrarTexto.place(x=190, y=253)      
        validarInfoB= tk.Button(self.ventana, text= "🔎", cursor="hand2", bg= "#0a509f",fg= "white",  width=2, height=1, relief="flat", command = lambda : (PageLoader.queryCedulas(self))) 
        validarInfoB.place(x=432, y=286)
        registroInfo= tk.Button(self.ventana, text= "Regístrate", cursor="hand2", bg= "#0a509f",fg= "white",  width=7, height=1, relief="flat", command = lambda : (ventanasMies.ventanaRegistro(self))) 
        registroInfo.place(x=150, y=332)   
    
    def ventanaRegistro(self):
        self.ventana.withdraw()
        self.ventanaRegistro=tk.Toplevel()
        self.ventanaRegistro.title("Registro de información")
        self.ventanaRegistro.geometry("600x600")
        self.ventanaRegistro.resizable(width="False", height="False")

        self.img = tkinter.PhotoImage(file = ingresarInfoFondo)
        Label(self.ventanaRegistro, image = self.img ).pack()

        ventanasMies.widgetsVentanaRegistro(self)

    def widgetsVentanaRegistro(self):
        '''
        Creación de cada uno los widgets a mostrar en la ventana de validación de la cédula
        '''

        '''Label texto primer nombre'''
        mostrarLabel=tk.Label(self.ventanaRegistro, text = "Nombre: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=95, y=125)
        '''Label texto segundo nombre'''
        mostrarLabel=tk.Label(self.ventanaRegistro, text = "Segundo Nombre: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=40, y=165)
        '''Label texto apellido'''
        mostrarLabel=tk.Label(self.ventanaRegistro, text = "Apellido: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=95, y=205)
        '''Label texto segundo apellido'''
        mostrarLabel=tk.Label(self.ventanaRegistro, text = "Segundo Apellido: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=40, y=245)
        '''Label texto género'''
        mostrarLabel=tk.Label(self.ventanaRegistro, text = "Género: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=400, y=125)
        '''Label texto cédula'''
        mostrarLabel=tk.Label(self.ventanaRegistro, text = "Cédula de Identidad: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=25, y=285)
        '''Label texto provincia'''
        mostrarLabel=tk.Label(self.ventanaRegistro, text = "Provincia: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=90, y=325)
        '''Label texto Cantón'''
        mostrarLabel=tk.Label(self.ventanaRegistro, text = "Cantón: ")
        mostrarLabel.config(bg= "#fafafb", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=105, y=365)
        '''Label texto edad'''
        mostrarLabel=tk.Label(self.ventanaRegistro, text = "Edad: ")
        mostrarLabel.config(bg= "#f4f4f4", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=115, y=405)

        '''Entradas de texto (Entrys)'''
        '''Entrada de texto del primer nombre'''
        nombreEntry=tk.Entry(self.ventanaRegistro, font=font.Font(family="Arial", size = "10"),textvar="", width=25, relief="flat")
        nombreEntry.place(x=180, y=125)
        '''Entrada de texto del segundo nombre'''
        nombre2Entry = tk.Entry(self.ventanaRegistro, font=font.Font(family="Arial", size = "10"),textvar="", width=25, relief="flat")
        nombre2Entry.place(x=180, y=165)
        '''Entrada de texto del primer apellido'''
        apellidoEntry = tk.Entry(self.ventanaRegistro, font=font.Font(family="Arial", size = "10"),textvar="", width=25, relief="flat")
        apellidoEntry.place(x=180, y=205)
        '''Entrada de texto del segundo apellido'''
        apellido2Entry = tk.Entry(self.ventanaRegistro, font=font.Font(family="Arial", size = "10"),textvar="", width=25, relief="flat")
        apellido2Entry.place(x=180, y=245)
        '''Entrada de texto de la ciudad del usuario'''
        cedulaEntry = tk.Entry(self.ventanaRegistro, font=font.Font(family="Arial", size = "10"),textvar="", width=25, relief="flat")
        cedulaEntry.place(x=180, y=285)
        '''Menu despegable para elegir la provincia y el cantón del usuario'''
        provinciaEntry = ttk.Combobox(self.ventanaRegistro, width=20, state="readonly")
        provinciaEntry.place(x=175, y=325)

class ventanaMiesAdmin():
    '''
    Clase ventana, se encarga de configurar la ventana
    y agregar widgets para que estos sean mostrados en la interfaz gráfica.
    ---
    Atributos
    -------
    ventana = tk
        Ventana a configurar
    Métodos:
    ----------
    __init__(self, ventana):
        Cosntructor de los atributos de la clase
    ventanasMies (self):
        Permite la configuración directa de la ventana.
    widgetsValidar (self):
        Mostrar por pantalla los widgets que se van a utilizar en la ventana principal

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

    def ventanaControl (self):
        '''
        Configuración de la ventana principal (validación de la cédula de identidad)
        '''
        self.ventana.tk.call('wm', 'iconphoto', self.ventana._w, tk.PhotoImage(file='icono.png'))
        self.ventana.title("BONO - MIES")
        self.ventana.config(bg="white")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        #self.ventana.resizable(width="False", height="False")
        
        
        #Asignación de un fondo al programa
        # self.img = tkinter.PhotoImage(file = logginFondo)
        # Label(self.ventana, image = self.img ).pack()



if __name__ == '__main__':
    conectarMongo = PageLoader(myClient) #Instancia para conectar a mongodb
    
    personaBono = personaMies("", "", "", "", "", "" , "", "", "", "", "ADMIN", "", "")
    listaRangos = conectarMongo.mostrarRoles()

    if personaBono.rol == listaRangos[0]:
        ventana = Tk()
        adminVentana=ventanaMiesAdmin(ventana)
        adminVentana.ventanaControl()
        ventana.mainloop()
    else: 
        print("USUARIO")

    # ventana = Tk()
    # window = ventanasMies (ventana)
    # #window.ventanasMies()
    # window.ventanaRegistro()
    # ventana.mainloop()

