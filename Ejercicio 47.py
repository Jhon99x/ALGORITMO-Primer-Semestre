'''Pide el precio de un producto y si es esencial o no, y aplica IVA según el tipo.'''

precio = float(input("Ingrese el precio del producto: "))
esencial = input("¿El producto es esencial? (si/no): ").strip().lower()

if esencial == "si":
    iva = 0.04
else:
    iva = 0.16

precio_final = precio + (precio * iva)
print("El precio final del producto es:", precio_final)