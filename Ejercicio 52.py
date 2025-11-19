'''Una empresa de alquiler de autos permite alquilar vehículos solo a personas mayores de
21 años. Sin embargo, si la persona tiene entre 21 y 25 años, se le cobra un cargo
adicional del 15%. Si es mayor de 25, no se cobra ningún cargo adicional. Escribe un
programa que determine si alguien puede alquilar un auto y el costo adicional si aplica.'''

edad = int(input("Ingrese su edad: "))
costo_alquiler = float(input("Ingrese el costo base del alquiler del auto: "))
if edad < 21:
    print("No puede alquilar un auto.")
elif 21 <= edad <= 25:
    cargo_adicional = costo_alquiler * 0.15
    print("Se aplica un cargo adicional del 15%. El costo total es:", costo_alquiler + cargo_adicional)
else:
    print("No se aplica cargo adicional. El costo total es:", costo_alquiler)
    