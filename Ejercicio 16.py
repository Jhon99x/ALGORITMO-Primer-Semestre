'''Pide una calificación y clasifícala en "Excelente", "Buena", "Regular" o "Mala".'''
print("Ingresa una nota:")
nota = float(input())

if nota <3:
    print("Su nota es mala.")
elif 3<= nota <=3.9:
    print("su nota es regular.")
elif 4<= nota <=4.4:
    print("Su nota es buena.")
elif 4.5<= nota <=5:
    print("Su nota es excelente.")