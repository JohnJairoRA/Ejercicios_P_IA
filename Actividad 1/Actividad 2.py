#imprimimos el texto con el programa a ejecutar
print ("Actividad 2 numeros del 1 al 100")

#solicitamos al usuario un numero del uno al 100 limitando y estableciendo la condicion
Numero = int(input("Ingresa un numero del 1 al 100: "))
# En las siguientes funiones utilizamos las condicionales if, elif y else
if Numero < 1:
    print ("Por favor ingresa un numero mayor a 0.")
elif Numero >=100: 
    print("Favor ingresar un número menor o igual a 100.")
else:
    print(f"¡Muy bien! el  {Numero} no es una gran opcion.")


