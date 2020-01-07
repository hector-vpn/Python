from tkinter.ttk import *
from tkinter import *

windows=Tk()
windows.title("Hola Mundo")
windows.geometry('350x350')
#Etiquetas
etiqueta1=Label(windows, text="Hola")
etiqueta1.grid(column=0,row=0)
#Agrega cuadro de texto
txt = Entry(windows,width=10)
txt.grid(column=1, row=0)
txt.focus()
def Clicked():
    """Esta funcion controla eventos """
    res="Bienvenido "+txt.get()
    etiqueta1.configure(text=res)
#agrega boton    
btn=Button(windows,text="Click Aqui", command=Clicked)
btn.grid(column=2,row=0)



windows.mainloop()
