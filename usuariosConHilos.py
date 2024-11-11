import threading

# Lista que usa diccionarios para almacenar la informacion de los usuarios
usuarios = [
    {"id": 1, "nombre": "Ana", "edad": 30},
    {"id": 2, "nombre": "Carlos", "edad": 22},
    {"id": 3, "nombre": "Beatriz", "edad": 27},
    {"id": 4, "nombre": "David", "edad": 35},
    {"id": 5, "nombre": "Elena", "edad": 29}
]

# Funcion que procesa la informacion de los usuarios
def procesarUsuarios(id, nombre, edad):
    print("ID: " + str(id) + " Nombre: " + nombre + " Edad: " + str(edad) )

# Se crea un hilo por cada usuario, se manda la informacion mediante args y kwargs
hilos = []
for usuario in usuarios:
    hilo = threading.Thread(target=procesarUsuarios, args=(usuario["id"],), kwargs={"nombre": usuario["nombre"],"edad": usuario["edad"]})
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()
