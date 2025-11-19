'''Pide una velocidad y clasifícala en "Baja", "Normal" o "Alta".'''
print("Ingresa una velocidad")
velocidad = int(input())

if velocidad <30:
    print("Su velocidad es baja.")
elif 30<= velocidad <= 59:
    print("Su vlocidad es normal.")
else:
    print("Su velocidad es alta.")