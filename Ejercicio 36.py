'''Pide un código de descuento y aplica un descuento específico si es válido.'''

codigo = "1234"

descuento = input("Ingresa codigo de descuento:")

if descuento == codigo:
    print("Tiene un descuento del 50%")
else:
    print("Codigo no valido")