'''Pide el ingreso anual y calcula el impuesto basado en tramos de ingresos.'''

uvt = 49799 #Unidad de valor tributario
ingreso = int(input("Escribe tu ingreso anual en peso $: "))
tramo = ingreso / uvt #tramo UVT
print(tramo)
if 0<= tramo <=1090:
    print("Paga 0%, de impuesto")
elif 1091<= tramo <=1700:
    print("Paga 19%, de impuesto, en valor $",0.19*ingreso)
elif 1701<= tramo <=4100:
    print("Paga 28%, de impuesto, en valor $",0.28*ingreso)
elif 4101<= tramo <=8670:
    print("Paga 33%, de impuesto, en valor $",0.33*ingreso)
elif 8671<= tramo <=18970:
    print("Paga 35%, de impuesto, en valor $",0.35*ingreso)
elif 18971<= tramo <=31000:
    print("Paga 37%, de impuesto, en valor $",0.37*ingreso)
elif tramo > 31000:
    print("Paga 39%, de impuesto, en valor $",0.39*ingreso)
