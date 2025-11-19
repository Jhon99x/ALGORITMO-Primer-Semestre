'''Pide las edades de tres personas y determina quién es el mayor y quién el menor.'''

edad1 = int(input("Ingrese la edad de la primera persona: "))
edad2 = int(input("Ingrese la edad de la segunda persona: "))
edad3 = int(input("Ingrese la edad de la tercera persona: "))

if edad1 >= edad2 and edad1 >= edad3:
    print("La primera persona es la mayor con", edad1, "años.")

if edad2 >= edad1 and edad2 >= edad3:
    print("La segunda persona es la mayor con", edad2, "años.")

if edad3 >= edad1 and edad3 >= edad2:
    print("La tercera persona es la mayor con", edad3, "años.")
    
if edad1 <= edad2 and edad1 <= edad3:
    print("La primera persona es la menor con", edad1, "años.")

if edad2 <= edad1 and edad2 <= edad3:
    print("La segunda persona es la menor con", edad2, "años.")

if edad3 <= edad1 and edad3 <= edad2:
    print("La tercera persona es la menor con", edad3, "años.")