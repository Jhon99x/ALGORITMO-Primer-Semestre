'''Escribe un programa que reciba una calificación numérica (0 a 100) y determine la
categoría de la nota: "Muy deficiente" (menos de 50), "Deficiente" (50-64), "Regular"
(65-74), "Buena" (75-89) y "Excelente" (90-100).'''

calificacion = float(input("Ingrese una calificacion numerica (0 a 100): "))
if calificacion < 50:
    print("Muy deficiente")
elif 50 <= calificacion <= 64:
    print("Deficiente")
elif 65 <= calificacion <= 74:
    print("Regular")
elif 75 <= calificacion <= 89:
    print("Buena")
elif 90 <= calificacion <= 100:
    print("Excelente")