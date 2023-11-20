import tkinter as tk

def opcion1():
    etiqueta.config(text="Opción 1 seleccionada")

def cerrar_ventana():
    reserva.destroy()

# Crear la ventana principal
reserva = tk.Tk()
reserva.title("")
reserva.geometry("800x600")
reserva.resizable(False, False)
reserva.overrideredirect(1)  # Eliminar el borde del título

# Obtener el ancho y la altura de la pantalla
ancho_pantalla = reserva.winfo_screenwidth()
altura_pantalla = reserva.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla // 2) - (800 // 2)
y = (altura_pantalla // 2) - (600 // 2)
reserva.geometry("800x600+{}+{}".format(x, y))

# Crear un marco central para organizar los elementos
marco_central = tk.Frame(reserva)
marco_central.pack(expand=True)

# Etiqueta y Entry para ingresar el ID de la reserva
etiqueta_reserva = tk.Label(marco_central, text="Ingresa el ID de tu reserva")
etiqueta_reserva.grid(row=0, column=0, pady=(100, 5))  # Ajustar el espaciado

entry_reserva = tk.Entry(marco_central)
entry_reserva.grid(row=1, column=0, pady=(0, 20))  # Ajustar el espaciado

# Botón debajo de la etiqueta y el Entry
boton_buscar = tk.Button(marco_central, text="Buscar", command=opcion1, compound=tk.LEFT)
boton_buscar.grid(row=2, column=0, pady=(0, 100))  # Ajustar el espaciado

# Botón para cerrar la ventana
boton_cerrar = tk.Button(marco_central, text="Cerrar", command=cerrar_ventana)
boton_cerrar.grid(row=3, column=0, pady=20)

# Etiqueta para mostrar la opción seleccionada
etiqueta = tk.Label(marco_central, text="")
etiqueta.grid(row=4, column=0, pady=20)

# Configurar el grid para que se expanda en el marco central
marco_central.grid_columnconfigure(0, weight=1)
marco_central.grid_rowconfigure(0, weight=1)
marco_central.grid_rowconfigure(1, weight=1)
marco_central.grid_rowconfigure(2, weight=1)

# Iniciar el bucle de la aplicación
reserva.mainloop()
