'''Pide una temperatura y verifica si está en rango de ebullición o congelación.'''

temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

if temperatura == 100:
    print("La temperatura está en el punto de ebullición del agua.")
elif temperatura == 0:
    print("La temperatura está en el punto de congelación del agua.")
