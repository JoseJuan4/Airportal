import tkinter as tk
from tkinter import messagebox
import subprocess

def opcion1():
    messagebox.showinfo("screen", "llamada screen")
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
    subprocess.run(["python", "login.py"])

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

# Crear la barra de menú
barra_menu = tk.Menu(ventana)

# Crear las opciones del menú
opcion_menu1 = tk.Menu(barra_menu, tearoff=0)
opcion_menu1.add_command(label="Vuelo", command=opcion1)
opcion_menu2 = tk.Menu(barra_menu, tearoff=0)
opcion_menu2.add_command(label="Asientos", command=opcion2)
opcion_menu3 = tk.Menu(barra_menu, tearoff=0)
opcion_menu3.add_command(label="Pasajeros", command=opcion3)
opcion_menu4 = tk.Menu(barra_menu, tearoff=0)
opcion_menu4.add_command(label="Confirmacion", command=opcion4)


# Agregar las opciones al menú principal
barra_menu.add_cascade(label="Vuelo", menu=opcion_menu1)
barra_menu.add_cascade(label="Asientos", menu=opcion_menu2)
barra_menu.add_cascade(label="Pasajeros", menu=opcion_menu3)
barra_menu.add_cascade(label="Confirmacion", menu=opcion_menu4)

# Configurar la barra de menú en la ventana
ventana.config(menu=barra_menu)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()