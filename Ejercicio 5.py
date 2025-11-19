'''Escribe un programa que le pida al usuario dos números y un operador (+, -, *, /) y
realice la operación correspondiente.'''

lista = []

for i in range(2):
    numeros = float(input("Ingrese dos numeros:"))
    lista.append(numeros)
operacion = int(input("Ingrese 0 para (+), 1 para (-), 2 para (*), o 3 para (/): "))
if operacion == 0:
    resultado = lista[0]+lista[1]
elif operacion == 1:
    resultado = lista[0]-lista[1]
elif operacion == 2:
    resultado = lista[0]*lista[1]
elif operacion == 3:
    resultado = lista[0]/lista[1]
print(resultado)

    