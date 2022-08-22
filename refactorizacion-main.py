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


    '''
    def __init__(self, ventana):
        '''
        Constructor de los parámetros a usar 
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
        self.entradaCedula=tk.Entry(ventana, font=font.Font(family="Arial", size = "10"),textvar="", width=32, relief="flat")
        self.entradaCedula.place(x=150, y=292)
        ventanasMies.widgetsValidar(self)

    def widgetsValidar (self):
        '''
        Creación de cada uno los widgets a mostrar en la ventana de validación de la cédula
        '''
        mostrarTexto=tk.Label(ventana, text = "Ingrese su cédula de identidad")
        mostrarTexto.config(bg= "white", font=font.Font(family="Arial", size = "10"))
        mostrarTexto.place(x=190, y=253)      
        validarInfoB= tk.Button(self.ventana, text= "🔎", cursor="hand2", bg= "#0a509f",fg= "white",  width=2, height=1, relief="flat") 
        validarInfoB.place(x=432, y=286)
        registroInfo= tk.Button(self.ventana, text= "Regístrate", cursor="hand2", bg= "#0a509f",fg= "white",  width=7, height=1, relief="flat", command = lambda : (ventanasMies.ejemplo(self))) 
        registroInfo.place(x=150, y=332)   
        

    def ejemplo (self):
        self.ventana.withdraw()   
        self.win=tk.Toplevel()
        self.win.geometry('750x350')  



if __name__ == '__main__':
    ventana = Tk()
    window = ventanasMies (ventana)
    window.ventanasMies()
    ventana.mainloop()

