'''Pide un puntaje de examen y determina en qué rango cae (por ejemplo, A, B, C, D, o F).'''

puntaje = float(input("Ingrese puntaje del examen (0 a 10):"))

if 0<= puntaje <=1.9:
    print("F")
if 2<= puntaje <=3.9:
    print("D")
if 4<= puntaje <=5.9:
    print("C")
if 6<= puntaje <=7.9:
    print("B")
if 8<= puntaje <=10:
    print("A")
