import tkinter as tk

from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk 
from pymongo import MongoClient  # Importa la clase MongoClient de pymong


###CREACION DE LA VENTANA Y SUS CONFIGURACIONES PARA CENTRARSE###################################################################33
# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Inicio sesion")

# Establecer las dimensiones de la ventana
ventana.geometry("400x300")

# Evitar que se pueda modificar el tamaño de la ventana
ventana.resizable(False, False)




def iniciar_sesion():
    username = nombre_usuario.get()
    password = contrasena.get()

    # Conéctate a la base de datos MongoDB
    cliente = MongoClient("mongodb://localhost:27017/")  # Reemplaza con la URL de tu base de datos
    db = cliente["fly"]
    colecciones_usuarios = db["usuario"]

    # Busca el usuario en la base de datos
    usuario_encontrado = colecciones_usuarios.find_one({"Usuario": username, "Contraseña": password})

    if usuario_encontrado:
        # Si el usuario es encontrado, muestra un mensaje y abre la ventana del menú
        ventana.destroy()
        menu()
    else:
        # Si el usuario no es encontrado, muestra un mensaje de error
        messagebox.showerror("Error de inicio de sesión", "Credenciales inválidas")

def registr():
    # Abre la ventana de registro
    rutaregistro = "/home/brama/Escritorio/AirportalPY/registro.py"

    # Abre el archivo de Python usando subprocess
    subprocess.Popen(['python3', rutaregistro])


def menu():
    # Abre la ventana del menú
    
    rutamenu = "/home/brama/Escritorio/AirportalPY/menu.py"

    # Abre el archivo de Python usando subprocess
    subprocess.Popen(['python3', rutamenu])














# Obtener el ancho y la altura de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
altura_pantalla = ventana.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla // 2) - (400 // 2)  # La mitad del ancho de la pantalla menos la mitad del ancho de la ventana
y = (altura_pantalla // 2) - (300 // 2)  # La mitad de la altura de la pantalla menos la mitad de la altura de la ventana

# Establecer las dimensiones de la ventana y su posición centrada
ventana.geometry("400x400+{}+{}".format(x, y))
###FIN DEL CENTRADO DE LA VENTANA###################################################################################################################






########################ELEMENTOS DE LA VENTANA##################################################################################################


# Agregar el logo
logo_imagen = Image.open("/home/brama/pruebabd/imagenes/logo.png")  # Reemplaza "ruta_del_logo.png" con la ruta real de tu imagen
logo_imagen = logo_imagen.resize((150, 100), Image.ANTIALIAS)  # Ajusta el tamaño del logo
logo = ImageTk.PhotoImage(logo_imagen)
logo_label = tk.Label(ventana, image=logo)
logo_label.image = logo  # Mantener una referencia
logo_label.pack(pady=10)

# Nombre de usuario
etiqueta_usuario = tk.Label(ventana, text="Nombre de Usuario:")
etiqueta_usuario.pack(pady=10)
nombre_usuario = tk.Entry(ventana)
nombre_usuario.pack()

# Contraseña
etiqueta_contrasena = tk.Label(ventana, text="Contraseña:")
etiqueta_contrasena.pack(pady=10)
contrasena = tk.Entry(ventana, show="*")
contrasena.pack()




# Botón de inicio de sesión
boton_inicio_sesion = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
boton_inicio_sesion.pack(pady=20)

# Boton de creacion de cuenta
boton_crear_cuenta = tk.Button(ventana, text="Crear cuenta", command=registr)
boton_crear_cuenta.pack(pady=20)

##############################FIN DE LOS ELEMENTOS DE LA PANTALLA#########################################################################################



# Ejecutar el bucle principal
ventana.mainloop()