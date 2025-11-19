'''Pide un número y muestra la raíz cuadrada si es positivo. Si es negativo, muestra un
mensaje diciendo que no tiene raíz real.'''
import math

numero = float(input("Ingresa un numero:"))
if numero > 0:
    raiz = math.sqrt(numero)
    print("La raiz cuadrada de ", numero, "es: ",raiz)
elif numero <0:
    print("Este numero no tiene raiz real.")