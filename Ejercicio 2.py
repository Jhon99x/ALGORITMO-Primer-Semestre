'''Escribe un programa que le pida al usuario tres números y determine cuál es el mayor.'''
lista = []

for i in range(3):
    num = float(input("Ingrese un numero: "))
    lista.append(num)
    
mayor = max(lista)


print("El numero mayor de los que ingreso es: ",mayor)




    