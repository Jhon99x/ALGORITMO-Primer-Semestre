'''Pide cinco calificaciones y calcula el promedio, luego muestra el nivel de desempeño
(bajo, medio, alto).'''
total=0
promedio = 0
for i in range(5):
    calificacion = float(input("Introduce la calificación:" ))
    total += calificacion
    promedio = total / 5
print(promedio)

if 0<= promedio < 2:
    print("Desempeño bajo.")
elif 2 <= promedio < 3.5:
    print("Desempeño medio.")
else:
    print("Desempeño alto.")