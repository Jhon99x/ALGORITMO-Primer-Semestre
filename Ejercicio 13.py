'''Pide dos letras e indica si son iguales o cuál es mayor alfabéticamente.'''

lista = []
for i in range(2):
    letras = input("Ingresa un caracter: ")
    lista.append(letras)
if lista[0]==lista[1]:
    print("iguales")
elif lista[0]>lista[1]:
    print(lista[0], "Es mayor que", lista[1])
    
