## RETO 1 - Información Personal

nombre = 'Brahian'
edad = '31'
ciudad = 'Bogotá'
profesion = 'Ingeniero de Sistemas'

print(f"Hola, ni nombre es {nombre}.")
print(f"Tengo {edad} años.")
print(f"Vivo en {ciudad}. ")
print(f"Soy {profesion}.\n")

## RETO 2 - Calculadora Basica

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

suma = (numero_1 + numero_2)
resta = (numero_1 - numero_2)
multiplicacion = (numero_1*numero_2)
division = (numero_1/numero_2)

print(f"Suma: {suma}.")
print(f"Resta: {resta}.")
print(f"Multiplicación: {multiplicacion}.")
print(f"División: {division}.\n")

## RETO 3 - Gestión de Productos

productos = [
    "Laptop",
    "Mouse",
    "Teclado",
    "Monitor",
    "Audifonos"
]

## Mostrar productos
print("Productos iniciales: \n")
for i in(productos):
    producto = print(f"{i}\n")

## Mostrar cuantos productos existen
print(f"Cantidad de Productos: {len(productos)} \n")

## Agregar un nuevo producto
new_product = input("Agregando producto: ")
productos.append(new_product)


## Eliminar un producto
delete_product = input("Eliminando producto: ")
productos.remove(delete_product)

## Mostrar nuevamente lista actualizada
print("\n Lista final: \n")
for i in(productos):
    print(f"{i}\n")

print(f"Cantidad final: {len(productos)} \n")


## RETO 4 - Analizador de Estudiantes

estudiantes = [{
    "nombre": "Brahian",
    "edad": 31,
    "nota": 4.5
},
{
    "nombre": "Melani",
    "edad": 26,
    "nota": 3.8
},
{
    "nombre": "Santiago",
    "edad": 3,
    "nota": 5
},
{
    "nombre": "Maryoly",
    "edad": 53,
    "nota": 4
},
{
    "nombre": "Jenny",
    "edad": 40,
    "nota": 2.5
}
]

## Mostrar todos los estudiantes
print("Estudiantes: \n")
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']} \nEdad: {estudiante['edad']} \nNota: {estudiante['nota']} \n")

## Mostrar el promedio general de las notas.
promedio = sum(estudiante['nota'] for estudiante in estudiantes) / len(estudiantes)
print(f"Promedio general de las notas: {promedio} \n")

## Mostrar quién obtuvo la nota más alta.
maxima = max(estudiantes, key=lambda x: x['nota'])
print(f"El estudiante con la nota más alta es: {maxima['nombre']} con una nota de {maxima['nota']} \n")

## Mostrar quién obtuvo la nota más baja.
minima = min(estudiantes, key=lambda x: x['nota'])
print(f"El estudiante con la nota más baja es: {minima['nombre']} con una nota de {minima['nota']} \n")

## Mostrar únicamente los estudiantes aprobados.
print("Estudiantes aprobados: \n")
for estudiante in estudiantes:
    if estudiante['nota'] >= 3:
        print(f"Nombre: {estudiante['nombre']} \nEdad: {estudiante['edad']} \nNota: {estudiante['nota']} \n")


## RETO 5 - Sistema de Usuarios

usuarios = [
    {
        "id": 1,
        "nombre": "Brahian",
        "email": "brahian@example.com",
        "activo": True
    },
    {
        "id": 2,
        "nombre": "Ana",
        "email": "ana@example.com",
        "activo": False
    },
    {
        "id": 3,
        "nombre": "Carlos",
        "email": "carlos@example.com",
        "activo": True
    }
]

def obtener_usuarios():
    return usuarios

def obtener_usuario_por_id(user_id):
    for usuario in usuarios:
        if usuario["id"] == user_id:
            return usuario
    return None

def obtener_usuarios_activos():
    return [usuario for usuario in usuarios if usuario["activo"]]
   
def agregar_usuario(nuevo_usuario):
    for usuario in usuarios:
        if usuario["id"] == nuevo_usuario["id"]:
            print("Error: Ya existe un usuario con ese ID.")
            return False
    usuarios.append(nuevo_usuario)
    return True


def eliminar_usuario(user_id):
    for usuario in usuarios:
        if usuario["id"] == user_id:
            usuarios.remove(usuario)
            return True
    return False

def buscar_usuarios_por_nombre(nombre):
    return [usuario for usuario in usuarios if nombre.lower() in usuario["nombre"].lower()]
    

## MENU
while True:
    print("\nSistema de Usuarios")
    print("1. Mostrar todos los usuarios")
    print("2. Mostrar usuario por ID")
    print("3. Mostrar usuarios activos")
    print("4. Agregar usuario")
    print("5. Eliminar usuario")
    print("6. Buscar usuarios por nombre")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        for usuario in obtener_usuarios():
            print(usuario)
    elif opcion == "2":
        user_id = int(input("Ingrese el ID del usuario: "))
        usuario = obtener_usuario_por_id(user_id)
        if usuario:
            print(usuario)
        else:
            print("Usuario no encontrado.")
    elif opcion == "3":
        for usuario in obtener_usuarios_activos():
            print(usuario)
    elif opcion == "4":
        user_id = int(input("Ingrese el ID del nuevo usuario: "))
        nombre = input("Ingrese el nombre del nuevo usuario: ")
        email = input("Ingrese el email del nuevo usuario: ")
        activo = input("¿El usuario está activo? (True/False): ").lower() == 'true'
        agregado = agregar_usuario({"id": user_id, "nombre": nombre, "email": email, "activo": activo})
        if agregado:
            print("Usuario agregado exitosamente.")
        else:
            print("Error: Ya existe un usuario con ese ID.")
    elif opcion == "5":
        user_id = int(input("Ingrese el ID del usuario a eliminar: "))
        if eliminar_usuario(user_id):
            print("Usuario eliminado exitosamente.")
        else:
            print("Usuario no encontrado.")
    elif opcion == "6":
        nombre = input("Ingrese el nombre del usuario a buscar: ")
        resultados = buscar_usuarios_por_nombre(nombre)
        if resultados:
            for usuario in resultados:
                print(usuario)
        else:
            print("No se encontraron usuarios con ese nombre.")
    elif opcion == "7":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")