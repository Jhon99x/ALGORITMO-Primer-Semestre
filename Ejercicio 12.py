'''Pide tres números y muestra si son todos pares, todos impares, o hay mezcla.'''

lista = []
for i in range(3):
    numeros = int(input("Ingresa un valor: "))
    lista.append(numeros)
for j in lista:
    if j %2 == 0:
        print(j, "Es par")
    else:
        print(j, "Es impar")