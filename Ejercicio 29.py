'''Pide dos números y un operador, y realiza una operación considerando casos especiales
de división.'''

operacion = 0
listanum = []
for i in range(2):
    numero = float(input("Ingresa un numero: "))
    listanum.append(numero)
operador = int(input("Seleccione un operador: 0(*),1(-),2(+),3(/):"))    

if operador == 0:
    operacion = listanum[0]*listanum[1]
    print(operacion)
elif operador == 1:
    operacion = listanum[0]-listanum[1]
    print(operacion)
elif operador == 2:
    operacion = listanum[0]+listanum[1]
    print(operacion)

if operador == 3:
    if listanum[1]<0:
        print("No se puede dividir entre 0")
    else:
        operacion = listanum[0]/listanum[1]
        print(operacion)    