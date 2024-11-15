'''
Nombre = input("Escribe tu nombre:")

#elif -permite evaluar otra expresion si es verdadera
#Operadores logicos - Permite encadenar varias expresiones logicas
#And = (y) /  Or = (o)
#And Evalua que todas las expresiones sean True(verdaderas)
#Or con que una de las expresiones sea True(Verdadera)

if Nombre == "Yessica":
    print("saludos", Nombre)
elif Nombre == "francy":
    print("Que bonito nombre") 
else:
    print ("Que nombre tan extraño")

''
nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))

if nombre == "yessica" and edad >=25:
    print("Que bonito nombre, ya eres adulta")
elif nombre == "Ana" and edad <=40:
    print("Que bonito nombre, ya eres joven")
else:
    print ("Saludos")

'''
#OR
nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))

if nombre == "yessica" or nombre == "john" or nombre == "maikol":
    print("Todo bien :D")
elif nombre == "Ana" and edad <=40:
    print("Que bonito nombre, ya eres joven")
