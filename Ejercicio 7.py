'''Pide un número y determina si es positivo, negativo o cero.'''
numero = float(input("Ingrese un numero: "))
if numero <0:
    print("Numero negatvo.")
elif numero >0:
    print("Numero positivo.")
else:
    print("El numero es 0.")