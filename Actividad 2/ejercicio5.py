#Ejercicio numero 5
#Imprimirmos el programa de facturas con un saludo
print ("Bienvenido a tus facturas")
#creamos un direccionario vacio para almacenar las facturas
facturas = {}
#Creamos un ciclo while no un menu opcional para el usuario
while True:
  print("1. Añadir factura")
  print("2. pagar factura")
  print("1. salir")
  opcion = int(input("selecciona la accion que deseas realizar:" ))
#Si la opcion es = 1 entonces
  if opcion == 1:
    n_factura =int(input("ingrese el numero de factura:"))
#Agregamos los costos de la factura en decimales el usuario ingresara el dato
    costo = float(input("ingrese el costo de la factura:"))
#llamamos el diccionario vacio a n_factura el valor que ingresa el usuario ingresando el costo
    facturas[n_factura] = costo
#Mostraremos el mensaje de factura ingresada correctamente
    print("factura ingresada correctamente.")
#Entonces si el usuario escoge 2
  elif opcion == 2:
#llamamos nuevamente n_facturas para que ingrese el valor
    n_factura = int(input("ingrese el numero de factura a pagar:"))
#factura lo destinamos numero de facturas para que se almacene en el diccionario facturas
    if n_factura in facturas: #Indentation fixed here
      costo = facturas[n_factura] #Indentation fixed here
      print (f"la factura {n_factura} tiene un costo de {costo}") #Indentation fixed here
# Se finaliza el ciclo con la opcion 3
  elif opcion == 3:
    break
#Error si ingresa el usuario una opcion no valida el programa mostrara un mensaje.
  else:
#mostrando un mensaje invalido hasta que se cumpla la condicion
    print("opcion invalida. Por favor selecciona una opcion valida.")
#Calcular los totales
#Nombramos la funcion total cobrado
total_cobrado = sum(facturas.values())
#Que sera la suma de las facturas en valores ingresados por el usuario
#Los pendientes_totales seran la suma de los valores ingresados de las facturas
pendientes_totales= sum(facturas.values())

#Se imprime el total de el valor cobrado por la factura y el tota de pendientes de la facturas
print(f"Total cobrado: {total_cobrado}")
print(f"Total pendientes: {pendientes_totales}")