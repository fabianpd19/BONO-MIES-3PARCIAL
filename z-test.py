# from tkinter import *
# from tkinter import ttk
# from logicaNegocios import *

# def cantones(provincia):
#     '''Creación de array de la colección de provincias, que solo contengan provincias'''
#     query = {"provincia": provincia}
#     specificFind = coleccionPyC.find(query)
#     array= []
#     for find in specificFind:
#         array = (find["cantones"])
#     return array


# def listaCantones():
#     '''Creación de array de la colección de provincias, que solo contengan provincias'''
#     coleccionTotal=coleccionPyC.find()
#     diccionario = {}
#     for busqueda in coleccionTotal:
#         provincia = busqueda["provincia"]
#         diccionario [provincia] = cantones(provincia)
#     return diccionario

# def on_combobox_select(event):
#     combobox1.set("")
#     combobox1.config(values=opciones[combobox.get()])


# root = Tk()
# screen_width = str(root.winfo_screenwidth())
# screen_height = str(root.winfo_screenheight())
# tamano = screen_width+"x"+screen_height
# root.geometry(tamano)

# opciones = listaCantones()

# combobox = ttk.Combobox(
#     root, width="30", state="readonly", values=tuple(opciones.keys())
#     )
# combobox.grid(row="5", column="1")
# combobox.bind("<<ComboboxSelected>>", on_combobox_select)

# combobox1 = ttk.Combobox(
#     root, width="30", state="readonly"
#     )
# combobox1.grid(row="6", column="1")

# root.mainloop()






#Import the tkinter library
from tkinter import *

#Create an instance of tkinter frame
win = Tk()

#Set the geometry
win.geometry("650x250")

#Creating a canvas
myCanvas =Canvas(win, bg="white", height=200, width=200)
cordinates= 10, 10, 200, 200
arc = myCanvas.create_arc(cordinates, start=0, extent=320, fill="red")
myCanvas.pack()

#Clearing the canvas
myCanvas.delete('all')

win.mainloop()



