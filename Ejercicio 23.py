'''Pide tres lados y verifica si pueden formar un triángulo.'''

total = 0
for i in range(3):
    angulo = int(input("Ingresa tres angulos:"))
    total += angulo
if total == 180:
    print("La suma de los tres angulos que ingreso, conforma un triangulo")
else:
    print("La suma de los tres angulos que ingreso, no conforma un triangulo")
