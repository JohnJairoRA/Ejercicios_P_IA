#Tema: Listas --Tuplas --- Diccionarios - Estructura de datos
#Compuestas por str, int, float,listas
# Listas se declaran como una variable y utilizan corchetes []
#Listas = []
#Lista = []---()--{}
#En phyton se inicia desde 0= "john" , 1= "juan" 
#La lista tiene posiciones o indices
#len solo da la longitud de los elementos dentro de la lista
"""

print(len(nombres))
print(type(nombres))



nombres[1]="Dulce"
print(nombres)
#Append -- Agregar nuevo elemento a la lista y queda al final
nombres.append("mateo")
print(nombres)

#insertar un nueva posicion
nombres.insert(4,"martha")
print(nombres)

#Eliminar un elemento de la lista
nombres.remove("juan")
print(nombres)

#delete -- borrar un elemento de la lista segun el indice
del nombres[4]
print(nombres) 

#Filtrar un dato
print(1991 in nombres)

"""
""""
nombres = ["maria","tomas","daniel","carlos","erica","ramiro","jose","hanna"]
print(nombres)
print("Bienvenidos a la fiesta", nombres[0:3])
print("lo sentimos no estas invitado",nombres[4:8])

for n in nombres:
    print("se inscribio en la lista:",n)
"""

""""
#print("Bienvenidos a la fiesta", nombres[0:3]) #inclusivo
#print("lo sentimos no estas invitado",nombres[3:8]) #exclusivo
nombres = ["maria","tomas","daniel","carlos","erica","ramiro","jose","hanna"]
print(nombres)

for i, n in enumerate(nombres):
    print("se inscribio en la lista",i,n)
"""
nombres = ["maria","tomas","daniel","carlos","erica","ramiro","jose","hanna"]
print(nombres)

#f-string - formateo elegante
for i,n in enumerate(nombres):
    #print("se inscribio",i,"en la lista:",n)
    print(f"se inscribio{n} en la lista con el indice{i}")

