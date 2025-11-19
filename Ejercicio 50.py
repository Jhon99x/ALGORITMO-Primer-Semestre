'''Pide dos números y determina si son pares o impares y si uno es múltiplo del otro.'''

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 % 2 == 0:
    print("El primer número es par.")
else:
    print("El primer número es impar.")

if num2 % 2 == 0:
    print("El segundo número es par.")
else:
    print("El segundo número es impar.")
    

if num1 % num2 == 0:
    print("El primer número es múltiplo del segundo.")
elif num2 % num1 == 0:
    print("El segundo número es múltiplo del primero.")
else:
    print("Ninguno de los números es múltiplo del otro.")