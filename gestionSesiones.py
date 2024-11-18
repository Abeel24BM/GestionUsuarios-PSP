"""
Ejercicio: Gestión de Sesiones de Usuarios con threading.local()
Objetivo: Crear una aplicación en Python que simule la gestión de sesiones de usuarios en un entorno multihilo, utilizando threading.local() para almacenar información específica de cada usuario sin interferencia entre hilos.

Instrucciones:
Crea una clase SesionUsuario que contenga:
Un método iniciar_sesion(nombre_usuario) que almacene el nombre de usuario en una variable local del hilo.
Un método mostrar_sesion() que imprima el nombre de usuario asociado al hilo actual.
En la función principal:

Instancia un objeto SesionUsuario.
Crea un objeto threading.local() llamado datos_sesion que almacenará información específica de cada hilo.
Define la función gestionar_sesion que:
Utilice datos_sesion para almacenar una instancia de SesionUsuario.
Inicie sesión con un nombre de usuario pasado como parámetro y luego muestre la sesión.
Crea e inicia varios hilos, cada uno con un nombre de usuario diferente, para simular sesiones de diferentes usuarios de manera concurrente.

Cada hilo debe mostrar el nombre del usuario correctamente sin interferencia de otros hilos.
"""
import threading

class SesionUsuario:
    def __init__(self):
        self.nombre_usuario = None
    
    def iniciar_sesion(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        print(f"Sesión iniciada para el usuario: {self.nombre_usuario}")

    def mostrar_sesion(self):
        if self.nombre_usuario:
            print(f"Usuario en la sesión actual: {self.nombre_usuario}")
        else:
            print("No hay ninguna sesión activa en este hilo.")

def gestionar_sesion(nombre_usuario):
    if not hasattr(datos_sesion, 'sesion_usuario'):
        datos_sesion.sesion_usuario = SesionUsuario() 
    datos_sesion.sesion_usuario.iniciar_sesion(nombre_usuario)
    datos_sesion.sesion_usuario.mostrar_sesion()

datos_sesion = threading.local()
usuarios = ["Ana", "Carlos", "Beatriz", "David", "Elena"]
hilos = []
for usuario in usuarios:
    hilo = threading.Thread(target=gestionar_sesion, args=(usuario,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()