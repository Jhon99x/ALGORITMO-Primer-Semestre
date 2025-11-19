'''Pide la edad y determina si la persona puede votar, y si es obligatorio (entre 18 y 70
años).'''

edad = int(input("Ingresa tu edad:"))

if 18<= edad <=70:
    print("Usted esta en la bligacion de votar ya que esta en la edad requerida.")
else:
    print("No puede votar.")