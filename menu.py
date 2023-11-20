import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
from tkcalendar import DateEntry  # Importa DateEntry de tkcalendar
from tkinter import ttk


# Crear la ventana principal
menu = tk.Tk()

# Establecer el título de la ventana
menu.title("SUPER MENU")




# Evitar que se pueda modificar el tamaño de la ventana
menu.resizable(False, False)

menu.configure(bg="white")  # Establecer el fondo de la ventana en blanco

# Obtener el ancho y la altura de la pantalla
ancho_pantalla = menu.winfo_screenwidth()
altura_pantalla = menu.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla // 2) - (950 // 2)  # La mitad del ancho de la pantalla menos la mitad del ancho de la ventana
y = (altura_pantalla // 2) - (550 // 2)  # La mitad de la altura de la pantalla menos la mitad de la altura de la ventana

# Establecer las dimensiones de la ventana y su posición centrada
menu.geometry("950x550+{}+{}".format(x, y))






##################################################PRUEBAS#############################################################################3

def opcion1():
    menu.configure(bg="red")
    


def opcion2():
    menu.configure(bg="blue")

def opcion3():
    menu.configure(bg="gold")



def opcion4():
    menu.configure(bg="gray")

def cambiar_color_naranja(boton):
    # Restaurar el color original de todos los botones
    for btn in [boton1, boton2, boton3, boton4]:
        btn.config(bg="#FFD700", activebackground="#FFD700", relief=tk.FLAT)
    # Cambiar el color del botón clicado a naranja fuerte
    boton.config(bg="#FFA500", activebackground="#FFA500", relief=tk.SUNKEN)



def resaltar_naranja(event):
    event.widget.config(bg="#FFA500", activebackground="#FFA500")

def restaurar_color(event):
    if event.widget.cget("relief") != tk.SUNKEN:
        event.widget.config(bg="#FFD700", activebackground="#FFD700")





##############FUNCION PARA ABRIR LA VENTANA DE RESERVA
def abrir_ventana_reserva():
    # Abre la ventana de registro
    rutareserva = "/home/brama/Escritorio/AirportalPY/reserva.py"

    # Abre el archivo de Python usando subprocess
    subprocess.Popen(['python3', rutareserva])


   
def actualizar_destinos(*args):
    origen_seleccionado = origen_combobox.get()
    
    # Filtrar destinos disponibles para evitar repetir el origen seleccionado
    destinos_disponibles = [destino for destino in estados_destinos[origen_seleccionado] if destino != origen_seleccionado]
    
    destino_combobox['values'] = destinos_disponibles
    destino_combobox.set(destinos_disponibles[0] if destinos_disponibles else '')





# Crear un marco para organizar los botones en la parte superior
marco_botones = tk.Frame(menu, background="#FFD700")
marco_botones.pack(side=tk.TOP, fill=tk.X)



###########CARGAR LAS IMAGENES################33
boton_vuelo = tk.PhotoImage(file="/home/brama/Escritorio/AirportalPY/imagenes/logo.png").subsample(2,2)
label_logo = tk.Label(marco_botones, image=boton_vuelo)



icono_vuelo = tk.PhotoImage(file="/home/brama/Escritorio/AirportalPY/imagenes/iconoavion.png").subsample(9,9)
label_iconovuelo = tk.Label(marco_botones, image=icono_vuelo)


icono_reserva = tk.PhotoImage(file="/home/brama/Escritorio/AirportalPY/imagenes/iconoreservar.png").subsample(9,9)
label_iconoreservar = tk.Label(marco_botones, image=icono_reserva)


icono_paseabordar = tk.PhotoImage(file="/home/brama/Escritorio/AirportalPY/imagenes/iconopaseabordar.png").subsample(9,9)
label_iconopaseabordar = tk.Label(marco_botones, image=icono_paseabordar)

icono_estatusvuelo = tk.PhotoImage(file="/home/brama/Escritorio/AirportalPY/imagenes/iconoestatusvuelo.png").subsample(9,9)
label_iconoestatusvuelo = tk.Label(marco_botones, image=icono_estatusvuelo)

##LOGO DE LA PARTE IZQUIERDA SUPERIOR
label_logo.grid(row=0, column=0, padx=10) 





boton1 = tk.Button(
    marco_botones,
    text="VUELO",
    command=lambda: [opcion1(), cambiar_color_naranja(boton1)],
    compound=tk.LEFT,
    image=icono_vuelo,
    bg="#FFD700",  # Color de fondo por defecto
    activebackground="#FFD700",  # Naranja claro cuando el mouse está sobre el botón
    bd=2,  # Borde del botón
    highlightthickness=0,  # Grosor del resaltado
    relief=tk.FLAT,  # Establecer el relieve del botón
    borderwidth=1,  # Ancho del borde
    width=120,  # Ancho del botón
)
boton2 = tk.Button(
    marco_botones,
    text="RESERVA",
    command=lambda: [opcion2(), cambiar_color_naranja(boton2),abrir_ventana_reserva()],
    compound=tk.LEFT,
    image=icono_reserva,
    bg="#FFD700",  # Color de fondo por defecto
    activebackground="#FFD700",  # Naranja claro cuando el mouse está sobre el botón
    bd=2,  # Borde del botón
    highlightthickness=0,  # Grosor del resaltado
    relief=tk.FLAT,  # Establecer el relieve del botón
    borderwidth=1,  # Ancho del borde
    width=120,  # Ancho del botón
)
boton3 = tk.Button(
    marco_botones,
    text="PASE DE ABORDAR",
    command=lambda: [opcion3(), cambiar_color_naranja(boton3)],
    compound=tk.LEFT,
    image=icono_paseabordar,
    bg="#FFD700",  # Color de fondo por defecto
    activebackground="#FFD700",  # Naranja claro cuando el mouse está sobre el botón
    bd=2,  # Borde del botón
    highlightthickness=0,  # Grosor del resaltado
    relief=tk.FLAT,  # Establecer el relieve del botón
    borderwidth=1,  # Ancho del borde
    width=190,  # Ancho del botón
)
boton4 = tk.Button(
    marco_botones,
    text="ESTATUS DE VUELO",
    command=lambda: [opcion1(), cambiar_color_naranja(boton4)],
    compound=tk.LEFT,
    image=icono_estatusvuelo,
    bg="#FFD700",  # Color de fondo por defecto
    activebackground="#FFD700",  # Naranja claro cuando el mouse está sobre el botón
    bd=2,  # Borde del botón
    highlightthickness=0,  # Grosor del resaltado
    relief=tk.FLAT,  # Establecer el relieve del botón
    borderwidth=1,  # Ancho del borde
    width=180,  # Ancho del botón
)

# Configurar eventos para resaltar el color naranja cuando el mouse entra o sale del botón
boton1.bind("<Enter>", resaltar_naranja)
boton1.bind("<Leave>", restaurar_color)
boton2.bind("<Enter>", resaltar_naranja)
boton2.bind("<Leave>", restaurar_color)
boton3.bind("<Enter>", resaltar_naranja)
boton3.bind("<Leave>", restaurar_color)
boton4.bind("<Enter>", resaltar_naranja)
boton4.bind("<Leave>", restaurar_color)













# Añadir botones a la ventana
boton1.grid(row=0, column=1, padx=10)
boton2.grid(row=0, column=2, padx=10)
boton3.grid(row=0, column=3, padx=10)
boton4.grid(row=0, column=4, padx=10)




# Crear un marco para los elementos adicionales
marco_adicional = tk.Frame(menu, bg="white")
marco_adicional.pack(pady=20)


# Lista de estados y destinos (puedes ajustarlos según tus necesidades)
estados_mexico = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua",
                  "Coahuila", "Colima", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "México",
                  "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo",
                  "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"]



# Diccionario que mapea estados a destinos
estados_destinos = {
    "Aguascalientes": estados_mexico,
    "Baja California": estados_mexico,
    "Baja California Sur": estados_mexico,
    # ... (continuar con otros estados)
}

# Combobox de origen
origen_combobox = ttk.Combobox(marco_adicional, values=estados_mexico, state="readonly")
origen_combobox.set(estados_mexico[0])
origen_combobox.grid(row=0, column=0, padx=10, pady=10)

# Combobox de destino
destino_combobox = ttk.Combobox(marco_adicional, state="readonly")
destino_combobox.set(estados_destinos[estados_mexico[0]][0])
destino_combobox.grid(row=0, column=1, padx=10, pady=10)


# Configurar el evento <<ComboboxSelected>> para el Combobox de origen
origen_combobox.bind("<<ComboboxSelected>>", actualizar_destinos)

# Combobox de fechas de ida
fecha_salida_label = tk.Label(marco_adicional, text="Fecha de Ida:")
fecha_salida_label.grid(row=1, column=0, padx=10, pady=10)
fecha_salida_entry = DateEntry(marco_adicional, background='darkblue', foreground='white', borderwidth=2)
fecha_salida_entry.grid(row=1, column=1, padx=10, pady=10)

# Combobox de fechas de regreso
fecha_regreso_label = tk.Label(marco_adicional, text="Fecha de Regreso:")
fecha_regreso_label.grid(row=2, column=0, padx=10, pady=10)
fecha_regreso_entry = DateEntry(marco_adicional, background='darkblue', foreground='white', borderwidth=2)
fecha_regreso_entry.grid(row=2, column=1, padx=10, pady=10)

# Combobox de categoría de pasajeros
categoria_pasajero_label = tk.Label(marco_adicional, text="Categoría de Pasajeros:")
categoria_pasajero_label.grid(row=3, column=0, padx=10, pady=10)
categorias_pasajeros = ["Adulto (>13)", "Menor (2-12)", "Bebé (0-23 meses)"]
categoria_pasajero_combobox = ttk.Combobox(marco_adicional, values=categorias_pasajeros, state="readonly")
categoria_pasajero_combobox.set(categorias_pasajeros[0])
categoria_pasajero_combobox.grid(row=3, column=1, padx=10, pady=10)










# Combobox de origen
origen_combobox.grid(row=0, column=0, padx=10, pady=10)

# Combobox de destino
destino_combobox.grid(row=0, column=1, padx=10, pady=10)

# Combobox de fechas de ida
fecha_salida_label.grid(row=1, column=0, padx=10, pady=10)
fecha_salida_entry.grid(row=1, column=1, padx=10, pady=10)

# Combobox de fechas de regreso
fecha_regreso_label.grid(row=2, column=0, padx=10, pady=10)
fecha_regreso_entry.grid(row=2, column=1, padx=10, pady=10)

# Otros elementos adicionales restantes
categoria_pasajero_label.grid(row=3, column=0, padx=10, pady=10)
categoria_pasajero_combobox.grid(row=3, column=1, padx=10, pady=10)





################################################# FIN DE LAS PRUEBAS #############################################################




# Ejecutar el bucle principal
menu.mainloop()