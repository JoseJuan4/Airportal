import tkinter as tk
from tkinter import messagebox

def opcion_nueva():
    messagebox.showinfo("Nueva Opción", "Has seleccionado una nueva opción")

# Crear la ventana secundaria
ventana_otro_archivo = tk.Tk()
ventana_otro_archivo.title("Otro Archivo")

# Crear la barra de menú en la nueva ventana
barra_menu_otro_archivo = tk.Menu(ventana_otro_archivo)

# Crear las opciones del menú en la nueva ventana
opcion_menu_otro_archivo = tk.Menu(barra_menu_otro_archivo, tearoff=0)
opcion_menu_otro_archivo.add_command(label="Nueva Opción", command=opcion_nueva)

# Agregar las opciones al menú principal de la nueva ventana
barra_menu_otro_archivo.add_cascade(label="Nueva Menu", menu=opcion_menu_otro_archivo)

# Configurar la barra de menú en la nueva ventana
ventana_otro_archivo.config(menu=barra_menu_otro_archivo)

# Iniciar el bucle de la interfaz gráfica de la nueva ventana
ventana_otro_archivo.mainloop()
