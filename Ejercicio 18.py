'''Pide la edad y calcula cuántos días ha vivido (aproximadamente).'''

edad = int(input("Ingresa tu edad: "))
meses = 12*edad     #Saber cuantos meses ha vivido.
dias = meses * 30   #Saber cuantos dias ha vivido aproximadamente.
print("Usted ha vivido aproximadamente",dias, "dias")