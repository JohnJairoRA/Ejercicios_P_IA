from datetime import datetime

print("*****************************")
print("*****   BIENVENIDO A    *****")
print("*** LA TIENDA DE MASCOTAS ***")
print("*****************************")

inventario = {"perro":10,
              "gato":8,
              "pajaro":25,
              "hamster":1}

animales_totales = 0
for val in inventario.values():
    animales_totales += val

nombre = input("Por favor ingresa tu nombre: ")
apellido = input("Por favor ingresa tu Apellido: ")

print("Gracias por visitarnos,", nombre, apellido)

compras = []

def mostrar_menu():
    print("")
    print("")
    print("Selecciona la opcion que deseas:")
    print("1. Conocer cuantas Mascotas tiene la Tienda")
    print("2. Comprar una Mascota")
    print("3. Mostrar compras")
    print("4. Salir del Programa")

def mostrar_inventario():
    print(" **** Inventario/Stock **** ")
    for llave, valor in inventario.items():
        print(f"   {llave}: {valor}")
    print("En total tenemos", animales_totales, "Mascotas")

def comprar_animal():
    carrito = []

    while True:
        print("¿Que Mascota deseas comprar?, Solo puedes elegir uno de c/d especie")
        print("Escribe F para terminar la lista de compras o V para ver tu carrito")

        animal = input()
        if animal == "F":
            break

        if animal == "V":
            print(f"Tu carrito de compra contiene {carrito}")
            continue

        if animal not in inventario:
            print(f"Lo setimos , no contamos con la mascota, {animal}")
        elif inventario[animal] == 0 : 
            print(f"Lo sentimos, no tenemos en existencia el, {animal}")
        elif animal not in carrito:
            carrito.append(animal)
        else:
            print("Esta mascota ya se encuentra en tu lista de compra")

    print("El contenido del carrito es")
    for animal in carrito:
        print("     ", animal)
        inventario[animal] -= 1
    #Agregar esta compra al carrito de compras 
    #Tupla: NombreAni, carrito, fecha
    fecha = datetime.now()
    compras.append((nombre, carrito, fecha))

def mostrar_compras():
    print("")
    print("****** Compras Realizadas *****")
    for compra in compras: 
        print(f"    {compra[0]} compró {compra[1]} el {compra[2]}")

while True:
    mostrar_menu()
    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comprar_animal()
    elif respuesta == 3: 
        mostrar_compras()
    elif respuesta == 4: 
        print("Saliendo del programa")
        break
    else:
        print("Ingresa una opción valida: ")
