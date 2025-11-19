'''Pide el monto de una transferencia y el saldo disponible, y detecta si la transacción es
fraudulenta.'''

saldo = int(input("Ingrese su saldo:"))
monto = int(input("Ingrese el monto:"))

if monto > saldo:
    print("Transaccion fraudulenta.")
else:
    print("Transaccion aprobada.")