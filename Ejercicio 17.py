'''Pide dos números y determina si el primero es múltiplo del segundo.'''
lista = []
print("Ingresa dos numeros:")
for i in range(2):
    numero = int(input())
    lista.append(numero)
resultado =  lista[0] % lista[1] 
if resultado == 0:
    print("Son multiplos")
else:
    print("No son multiplos")

