'''Pide dos números y muestra cuál está más cerca de 100.'''
lista = []
print("Ingresa dos valores:")

for i in range(2):
    numero = float(input())
    lista.append(numero)
if abs(100-lista[0])< abs(100-lista[1]):  #abs es una funcion que significa valor absoluto.
    print(lista[0],"Esta mas cerca de 100")
else:
    print(lista[1],"Esta mas cerca de 100")