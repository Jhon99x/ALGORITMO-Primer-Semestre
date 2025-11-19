'''Escribe un programa que le pida al usuario su calificación y determine si aprobó (60 o
más), reprobó (menos de 60), y si es un aprobado especial (90 o más).'''

calificacion = float(input("Ingrese su nota academica:"))
#if calificacion >= 60:
    #print("Aprobo.")
if 60<= calificacion <90:
    print("Aprobo.")
elif calificacion >= 90:
    print("Aprobado con honor.")
else:
    print("Reprobo.")