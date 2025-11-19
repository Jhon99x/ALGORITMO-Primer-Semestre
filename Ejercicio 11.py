'''Pide un año y determina si es bisiesto.'''
año = int(input("Ingrese un año:"))
if año %4 == 0:
    print(año, "Es bisiesto.")
else:
    print(año, "No es bisiesto.")