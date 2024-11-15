#Ejercicio 4
print ("Bienvenido al programa de asignaturas estudiante")
print("Ingresa tus datos:")
print("*********************************************")
persona = {
    "nombre": input("ingrese su nombre:"),
    "edad": input("ingrese su edad:"),
    "direccion": input("ingrese su direccion:"),
    "telefono": input("ingrese su telefono:")
}
print(persona)
print("*********************************************")

print ("Ingresa tus notas:")
print("*********************************************")

# creamos una lista llamada repetir lista vacia
Repetir = []

# iteramos atraves de las notas para obtener las calificaciones
for nota in tus_notas: #reemplazamos tus_notas por nota
    while True:  # utilizamos un ciclo while para validar si es verdadero
        try: #Lo usamos para utilizar una excepcion
#Utilizamos un valor que el usuario ingresara llamado nota_valor utilizando
#float para representar un valor positivo y negativo en nota se almacenara en la
#lista en un rango de 0 a 10 valor de la calificacion
            nota_valor = float(input(f"ingrese la nota de la asignatura {nota} (0-10):"))
#si 0 es menor o igual a el valor que ingresa eñ usuario finaliza el ciclo
            if 0 <= nota_valor <= 10:
                break #fin del ciclo
            else: #se imprimira que ingrese un numero valido
                print("numero de nota errada. Ingrese un valor valido entre 0 y 10.")
        except ValueError: #usamos una excepcion cuando indique un valor errado dentro de try
                #valueerror es el valor incorrecto que ingresa el usuario
            print("valor invalido. Por favor ingrese un número.")
            #Se imprimira

    #Si el valor ingresado es menor a 5
    if nota_valor < 5:
        Repetir.append(nota)
#Hace un llamado de la lista e ingresa los datos con append a la lista nota

#si repetir cumple las condiciones imprimira de la lista nota en Repetir
if Repetir:
    print("reprobaste debes repetir:")
    for nota in Repetir: #
        print(nota)
#Si el valor es mayor a 5 imprimira que aprobo las notas
else:
    print("¡Felicidades! pasaste tus notas.")

#Si el usuario desea validar la nota de otro estudiante podra repetir el ciclo
Deseas_continuar = input("¿DEseas ingresar notas de otro estudiante? (s/n):")
if Deseas_continuar.lower() != "s":
    pass #Su uso es para bucles que no se le ha determinado una funcion en este caso sirve para evitar errores
