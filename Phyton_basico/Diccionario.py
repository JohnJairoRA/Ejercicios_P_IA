#Diccionarios: Arreglos asociativos
#lista de elementos Llave:Valor <--- Diccionario

persona ={"Nombre":"Guillermo",
        "Edad":33,
        "Apellido:":"Parejo",
        "profecion:":"ingeniero"}


#persona["Apellido:"]="Pacheco"
#print(persona)
persona["Apodo:"]="Guillo"
#print(persona["Edad:"])
print(persona)

print(persona.keys()) #Lista de elementos de distintas llaves
print(persona.values()) #Devuelve los valores de las llaves
print(persona.items())#Devuelve todos los datos = Tuplas

for key in persona.keys():
    print(key)

for val in persona.values():
    print(val)

for it in persona.items():
    print(it)

for key, Value in persona.items():
    print(f"la llave {key} tiene valor {Value}")

print("profesion:" in persona)  #True
#print("profesion" in persona)   #False
