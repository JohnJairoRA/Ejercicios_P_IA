# Nombre de la tienda
print("********¡Tienda_de frutas!********")

# Ingreso de nombre y saludo de bienvenida 
nombre = input("Ingresa tu nombre: ")
apellidos = input("Ingresa tu apellido: ")

# Formatear una cadena de texto de saludo de bienvenida
print(f"¡Encantado de conocerte, {nombre} {apellidos}!")

# Cantidades de frutas creamos un diccionario 1
inventario = {"melones": 50, "peras": 20, "manzanas": 40, "bananos": 60, "naranjas": 15}

# Precios de cada fruta diccionario 2
precios = {"melones": 1000, "peras": 2000, "manzanas": 3000, "bananos": 4000, "naranjas": 5000}

# Definimos mostrar_tienda_frutas como menu opcional
def mostrar_tienda_frutas():
    print("\nSelecciona la fruta que deseas comprar:")
    print("1. Melones")
    print("2. Peras")
    print("3. Manzanas")
    print("4. Bananos")
    print("5. Naranjas")
    print("6. Salir")

# Mostrar menú
mostrar_tienda_frutas()

# Se define la seleccion_fruta y se convierte a entero
seleccion_fruta = int(input("Ingresa el número de la fruta que deseas comprar: "))

# Función para procesar la compra usamos la condicional if(si) para comparar
def compra(fruta):
    cantidad = int(input(f"¿Cuántos {fruta} deseas comprar? "))
    if inventario[fruta] >= cantidad:
        total = cantidad * precios[fruta]
        inventario[fruta] -= cantidad
        print(f"Has comprado {cantidad} {fruta}. Total a pagar: ${total}. Inventario restante: {inventario[fruta]}")
    else:
        print(f"Lo siento, no tenemos suficientes {fruta}. Inventario disponible: {inventario[fruta]}")

# Función para mostrar compras (aquí necesitas definir la variable 'compras' correctamente)
def mostrar_compras():
    print("")
    print("********compras realizadas********")
    for compra in compras: 
        print(f"    {compra[0]} compró {compra[1]} el {compra[2]}")

# Seleccionar fruta del menú
while True:
    mostrar_tienda_frutas()
    seleccion_fruta = int(input())

    if seleccion_fruta == 1:
        print("Has seleccionado melones")
        compra("melones")
    elif seleccion_fruta == 2:
        print("Has seleccionado peras")
        compra("peras")
    elif seleccion_fruta == 3:
        print("Has seleccionado manzanas")
        compra("manzanas")
    elif seleccion_fruta == 4:
        print("Has seleccionado bananos")
        compra("bananos")
    elif seleccion_fruta == 5:
        print("Has seleccionado naranjas")
        compra("naranjas")
    elif seleccion_fruta == 6:
        print("Gracias por visitar la tienda de frutas. ¡Hasta luego!")
        break
    else:
        print("Selección inválida. Por favor, intenta de nuevo.")