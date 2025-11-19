'''Un supermercado ofrece descuentos en función de la hora de compra. Si la compra es
antes de las 12:00 p.m., se aplica un 10% de descuento. Si la compra es después de las
6:00 p.m., el descuento es del 20%. En otros horarios, no hay descuento. Escribe un
programa que determine el descuento aplicable y el total a pagar.'''

hora = float(input("Ingrese la hora de su compra (formato 24 horas, ej. 13.30 para 1:30 p.m.): "))
if hora < 12.00:
    print("Se aplica un 10%, de descuento.")
elif hora > 18.00:
    print("Se aplica un 20%, de descuento.")
else:
    print("No hay descuento.")
    
total = float(input("Ingrese el total de su compra: "))

if hora < 12.00:
    descuento = total * 0.10
elif hora > 18.00:
    descuento = total * 0.20
else:
    descuento = 0

total_pagar = total - descuento
print("El total a pagar después del descuento es:", total_pagar)