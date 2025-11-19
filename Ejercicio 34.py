'''Pide la categoría del cliente y calcula el descuento en base a la categoría.'''

categoria = ["a","b","c"]

cliente = input("Ingrese la categoria:")

if cliente == "a":
    print("Tiene un descuento del 30%")
elif cliente == "b":
    print("Tiene un descuento del 20%")
elif cliente == "c":
    print("Tiene un descuento del 10%")
