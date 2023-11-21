import tkinter as tk
from tkinter import messagebox
import subprocess

def opcion1():
    abrir_otro_archivo()

def opcion2():
    messagebox.showinfo("screen", "llamada screen")
def opcion3():
    messagebox.showinfo("screen", "llamada screen")

def opcion4():
    messagebox.showinfo("screen", "llamada screen")

def opcion5():
    messagebox.showinfo("screen", "llamada screen")

def abrir_otro_archivo():
    subprocess.run(["python3","login.py"])



# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sub menu")
# Evitar que se pueda modificar el tamaño de la ventana
ventana.resizable(False, False)
ventana.configure(bg="white")  # Establecer el fondo de la ventana en blanco
# Obtener el ancho y la altura de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
altura_pantalla = ventana.winfo_screenheight()
# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla // 2) - (950 // 2)  # La mitad del ancho de la pantalla menos la mitad del ancho de la ventana
y = (altura_pantalla // 2) - (550 // 2)  # La mitad de la altura de la pantalla menos la mitad de la altura de la ventana
# Establecer las dimensiones de la ventana y su posición centrada
ventana.geometry("950x550+{}+{}".format(x, y))
# Crear un marco para organizar los botones en la parte superior
marco_botones = tk.Frame(ventana, background="#FFD700")
marco_botones.pack(side=tk.TOP, fill=tk.X)

#LOGO DE LA PARTE IZQUIERDA SUPERIOR
logo= tk.PhotoImage(file="imagenes/logo.png").subsample(2,2)
label_logo = tk.Label(marco_botones, image=logo)
label_logo.grid(row=0, column=0, padx=10) 

op1 = tk.PhotoImage(file="imagenes/iconoavion.png").subsample(9,9)
label_iconovuelo = tk.Label(marco_botones, image=op1)

op2 = tk.PhotoImage(file="imagenes/iconoasiento.png").subsample(9,9)
label_iconoreservar = tk.Label(marco_botones, image=op2)

op3 = tk.PhotoImage(file="imagenes/iconoboleto.png").subsample(9,9)
label_iconoreservar = tk.Label(marco_botones, image=op3)

op4 = tk.PhotoImage(file="imagenes/cheque.png").subsample(9,9)
label_iconoreservar = tk.Label(marco_botones, image=op4)

#botones menu
boton1 = tk.Button(
    marco_botones,
    text="VUELO",
    command=lambda: [opcion1()],
    compound=tk.LEFT,
    image=op1,
    bg="#FFD700",  # Color de fondo por defecto
    activebackground="#FFD700",  # Naranja claro cuando el mouse está sobre el botón
    bd=2,  # Borde del botón
    highlightthickness=0,  # Grosor del resaltado
    relief=tk.FLAT,  # Establecer el relieve del botón
    borderwidth=1,  # Ancho del borde
    width=120,  # Ancho del botón
)
#añadir bnt screen
boton1.grid(row=0, column=1, padx=10)

boton2 = tk.Button(
    marco_botones,
    text="ASIENTOS",
    command=lambda: [opcion2()],
    compound=tk.LEFT,
    image=op2,
    bg="#FFD700",  # Color de fondo por defecto
    activebackground="#FFD700",  # Naranja claro cuando el mouse está sobre el botón
    bd=2,  # Borde del botón
    highlightthickness=0,  # Grosor del resaltado
    relief=tk.FLAT,  # Establecer el relieve del botón
    borderwidth=1,  # Ancho del borde
    width=120,  # Ancho del botón
)
boton2.grid(row=0, column=2, padx=10)

boton3 = tk.Button(
    marco_botones,
    text="PASAJEROS",
    command=lambda: [opcion3()],
    compound=tk.LEFT,
    image=op3,
    bg="#FFD700",  # Color de fondo por defecto
    activebackground="#FFD700",  # Naranja claro cuando el mouse está sobre el botón
    bd=2,  # Borde del botón
    highlightthickness=0,  # Grosor del resaltado
    relief=tk.FLAT,  # Establecer el relieve del botón
    borderwidth=1,  # Ancho del borde
    width=120,  # Ancho del botón
)
boton3.grid(row=0, column=3, padx=10)

boton4 = tk.Button(
    marco_botones,
    text="CONFRIRMACION",
    command=lambda: [opcion4()],
    compound=tk.LEFT,
    image=op4,
    bg="#FFD700",  # Color de fondo por defecto
    activebackground="#FFD700",  # Naranja claro cuando el mouse está sobre el botón
    bd=2,  # Borde del botón
    highlightthickness=0,  # Grosor del resaltado
    relief=tk.FLAT,  # Establecer el relieve del botón
    borderwidth=1,  # Ancho del borde
    width=160,  # Ancho del botón
)
boton4.grid(row=0, column=4, padx=10)





# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()