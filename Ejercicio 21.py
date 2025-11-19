'''Calcula el promedio de tres notas y determina si el estudiante aprueba o reprueba
(mínimo 60).'''
total = 0
print("Ingrese las 3 notas")
for i in range(3):
    nota = int(input())
    total += nota
print("Total de la nota es:",total)
resultado = total / 3
if resultado >=60:
    print("Aprobado")
else:
    print("Reprobado")