
'''
#ciclos -bucles - interaccion
#Repeticion de un conjunto de instrucciones.
#Ciclo for --ciclo while -- Coclo white True

#Ciclo for - Es aquel para que se ejecute un conjunto de instrucciones un numero determinado de veces

for Variable in <expresion>:
    Bloque de instrucciones

''

for x in range(1,10):
    print(x)

''
#Ejemplos:

Lista = "John"
for item in Lista:
    print(item, end="")

''
Lista = ["a","E","i","o","u"]
Lista2= [1,2,3,4,5]
for item in Lista2:
    print("interaccion numero: " +str(item))
    for letra in Lista:
        print(letra,end=" ")
    print("\n")

''
#while
#Mientras se cumpla la condicion se ejecuta el ciclo w
i=1
while i<11:
    print(i)
    i = i+1

''''''    
#while
i=0
#while condicion:
while i< 10:
    if i<5:
        print("El numero de la interaccion es menor a 5")
    else:
        print("El numero",i,"Es mayor o igual a 5")
    i += 1 
''
pedirnumero = True
While pedirnumero:
    Valor = int(input("introduce un numero entero inferior a 10: "))
    if valor<10:
        pedirnumero = False
        print("Fin: Has introducido un numero inferior a 10")

'''''''''
#While True
while True:
    print("Escribe la opcion deseada")
    print("1. Saludar")
    print("2. Salir")

    respuesta = int(input())

    if respuesta ==1:
        print ("saludos, como vas")
    elif respuesta ==2:
        break
    print("Termino el programa") 
