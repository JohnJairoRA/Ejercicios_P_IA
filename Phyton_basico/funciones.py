#las funciones estan predefinidas son bloques del codigo fuente print(),type(),range(),input(), float()
# etc
#las funciones tienen un nombre sintaxis
#def=definir una funcion
#def Nombre de la funcion(parametros):
        #Bloque de instrucciones
        #Return valor del retorno

def Hola():
    print("¡Hola! como vas con python" )
Hola()


#Variables - Var = Nombre de la funcion(Parametros)
"""
def esparoimpar(param):
    if param%2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
numero = int(input("introduce un numero:"))
esparoimpar(numero)

"
def multiplicar(param1,param2):
    return param1*param2

multiplicando = int(input("introduce un numero: "))
multiplicador = int(input("introduce un numero: "))

resultado = multiplicar(multiplicando,multiplicador)
print("El resultado de la multiplicacion es:",resultado)

"""
#conversor de temperatura
#celsius - fahrenheit : (c*1.8)+32
def convertir_a_fahrenheit(c):
    return (c*1.8)+32 #Regrese el valor
celsius=32
fahrenheit = convertir_a_fahrenheit(celsius)
print(fahrenheit)












