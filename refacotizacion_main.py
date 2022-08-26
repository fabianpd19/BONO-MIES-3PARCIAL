import tkinter as tk
import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from turtle import width
from feriados import *
from logicaNegocios import *
import re

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
        self.ventana.withdraw()
        self.ventanaAgregarInfo=tk.Toplevel()
        self.ventanaAgregarInfo.title("Registro de información")
        self.ventanaAgregarInfo.geometry("600x600")
        self.ventanaAgregarInfo.resizable(width="False", height="False")

        self.img = tkinter.PhotoImage(file = ingresarInfoFondo)
        Label(self.ventanaAgregarInfo, image = self.img ).pack()
        
    def ventanaRegistroW(self):
        ventanasMies.ventanaRegistro(self)
        ventanasMies.widgetsVentanaRegistro(self)
    
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
        mostrarLabel=tk.Label(self.ventanaAgregarInfo, text = "Estados: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
        mostrarLabel.place(x=360, y=205)

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

        self.cantonEntry = ttk.Combobox(self.ventanaAgregarInfo, width=20, state="readonly")
        self.cantonEntry.place(x=175, y=365)

        self.generoEntry = ttk.Combobox(self.ventanaAgregarInfo, value= conectarMongo.listaGeneros(), width=10, state="readonly")
        self.generoEntry.place(x=425, y=125)

        self.estadoEntry = ttk.Combobox(self.ventanaAgregarInfo, value= conectarMongo.estadosUsuarios(), width=15, state="readonly")
        self.estadoEntry.place(x=425, y=205)

        #botones
        getDatosBoton= tk.Button(self.ventanaAgregarInfo, text= "Ingresar Datos", 
            cursor="hand2", bg= "#0a509f",fg= "white",  
            width=10, height=1, relief="flat", 
            command = lambda :  (getDatos(
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
                self.hijosEntry.get()
            )))
        getDatosBoton.place(x=400, y=464)

    def mostrarInformacion(self):
        
        '''Inicializaición de la ventana'''
        self.ventana.withdraw()
        self.ventanaMostrarInf = tk.Toplevel()
        self.ventanaMostrarInf.title("Datos")
        self.ventanaMostrarInf.geometry("600x600")
        self.ventanaMostrarInf.resizable(width="False", height="False")

        self.img = tkinter.PhotoImage(file = datosUsuarioFondo)
        Label(self.ventanaMostrarInf, image = self.img ).pack()
        
        #asignación del fondo
        texto1=tk.Label(self.ventanaMostrarInf, text = "Datos del Usuario")
        texto1.config(bg= "white", fg="#4779b2",font=("Arial", 11, "bold"))
        texto1.place(x=1, y=100)
        '''Texto de nombres'''
        query={"cedula": personaMies.cedula}
        find = conectarMongo.coleccionPersonas.find()
        specificFind = conectarMongo.coleccionPersonas.find(query)
        for find in specificFind:
            '''Mostrar el número de cédula en la ventana'''
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

            '''Mostrar el número de cédula en la ventana'''
            aprobadoLabel=tk.Label(self.ventanaMostrarInf, text = "Beneficiario: ")
            aprobadoLabel.config(bg= "white", fg="#4779b2",font=("Arial", 10, "bold"))
            aprobadoLabel.place(x=290, y=200)
            if (find["beneficiario"] == "SI"):        
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
    __init__(self, ventana):
        Cosntructor de los atributos de la clase
    ventanasMies (self):
        Permite la configuración directa de la ventana.
    widgetsValidar (self):
        Mostrar por pantalla los widgets que se van a utilizar en la ventana principal

    '''

    def ventanaControl (self):
        '''
        Configuración de la ventana principal (validación de la cédula de identidad)
        '''
        self.ventana.title("BONO - MIES")
        self.ventana.config(bg="white")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))

def validarCedula(cedula):
    '''
    Devolver true si está o false si no está el dato a buscar en la base de datos
    '''
    cedulasTotal=conectarMongo.queryCedulas()
    if cedula in cedulasTotal:
        personaMies.cedula=cedula
        validarRango()
    else:
        messagebox.showwarning("Error", "Ingrese una cédula de identidad válida.")

def on_combobox_select(event):
    window.cantonEntry.set("")
    window.cantonEntry.config(values=conectarMongo.diccionarioPyC()[window.provinciaEntry.get()])
    pass

def getDatos (nombre, nombre2, apellido, apellido2, provincia, canton, cedula, edad, genero, estado, correoElectronico, hijos):
    email_validate_pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    '''Validación de los datos'''
    '''Validar que no existan números en las cadenas a ingresar'''
    if validarDatos(nombre) == False:
        if validarDatos(nombre2) == False:
            if validarDatos(apellido) == False:
                if validarDatos(apellido2) == False:
                    personaBono.cedula = cedula
                    '''Validar que la edad sea un número y comprobar que sea mayor de 18 años y menor a 100'''
                    if edad.isnumeric():
                        if int(edad)>=18 and int(edad)<=65:
                            '''Validar que la cédula contenga solo números y que sea igual a 10 digitos'''
                            if cedula.isnumeric():
                                if len(personaBono.cedula) == 10:
                                    if hijos.isnumeric():
                                            if re.search(email_validate_pattern, correoElectronico):
                                                messagebox.showinfo("Datos Ingresados", "¡Datos ingresados correctamente!")
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
                                                updateDataBase=conectarMongo.coleccionPersonas.insert_one(diccionario)
                                            else:
                                                messagebox.showwarning("Error", "Ingrese un correo electrónico válido.")
                                    else:
                                        messagebox.showwarning("Error", hijos + " no es un valor válido")
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

def validarRango():
    query={"cedula": personaMies.cedula}
    find = conectarMongo.coleccionPersonas.find()
    specificFind = conectarMongo.coleccionPersonas.find(query)
    for find in specificFind:
        if find["rol"] == "ADMIN":
            ventana = Tk()
            adminVentana=ventanaMiesAdmin(ventana)
            adminVentana.ventanaControl()
        else:
            window.mostrarInformacion()

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
        window.ventanaRegistroW()

if __name__ == '__main__':
    conectarMongo = PageLoader(myClient)
    '''Instancia de la clase a PageLoader para poder conectar a MongoDB'''

    '''Instancia de Tkinter tanto como de la clase ventanasMies para abrir la ventana principal'''
    ventana = Tk()
    window = ventanasMies (ventana)

    '''Llamamos a la ventana principal'''
    window.ventanasMies()
    
    '''Instancia de la clase personaMies'''
    personaBono = personaMies("", "", "", "", "", "", "", "", "", "", "", "", "")

    '''Función mainloop'''
    ventana.mainloop()

    

