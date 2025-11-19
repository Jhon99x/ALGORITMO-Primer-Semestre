'''Crea un programa que pida la edad de una persona y determine
si es un nino(0-12 anos), un adolescente (13-17), un adulto (18-64)
o un adulto mayor (65 anos o mas)'''

edad = int(input("Ingrese su edad:"))

if edad <= 12:
    print("Es un nino:")
elif 13<= edad <=17:
     print("Adolescente")
elif 18<= edad <=64:
    print("Adulto")
else:
    print("adulto mayor")