#random
import random
#randint(min,max)
"""

resultado =  random.randint(1,100)
print(resultado)
"""
def tirar_dados():
    return random.randint(2,12)

def pedir_respuesta():
    print("ingresa tu prediccion")
    print("1. par")
    print("2. impar")
    print("3. salir del juego")
    
    respuesta = int(input())
    return respuesta    

def imprimir_resultado(numero,prediccion):
    #not,%
    #saber si un numero es par o impar
    #Dividirlo entre 2 si el resultado es 0,es par si es 1, es impar
    #5/2 = 2 == residuo es 1 === 6/2 resultado es 3 residuo es  0
    es_par =numero % 2 == 0
    #es par, prediccion= 1: Gane
    #no es par. prediccion =2, Gane
    #perdi
    if es_par and prediccion == 1:
        print("Ganaste! numero de los dados:", numero)
    elif not es_par and prediccion == 2:
        print("Ganaste! numero de los dados", numero)
    else:
        print("perdiste numero de los dados", numero)

while True:
    numero = tirar_dados()
    prediccion = pedir_respuesta()
    if prediccion == 3:
        break  
    imprimir_resultado(numero,prediccion)
print("gracias por jugar")
#print("Tiro de dados", tirar_dados())


