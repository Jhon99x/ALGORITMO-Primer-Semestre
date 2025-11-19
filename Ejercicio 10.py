'''Pide la edad y determina el descuento: 50% si es menor de 12, 20% si es mayor de 65, y
sin descuento para los demás.'''

edad = int(input("Ingrese su edad: "))
if edad <12:
    print("Su descuento es del 50%")
elif 13<= edad <=65:
    print("Su descuento es del 20%")
else:
    print("No tiene descuento.")