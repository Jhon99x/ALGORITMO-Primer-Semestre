'''Pide el número de horas trabajadas y calcula el salario con 50% más para horas extra.'''
salario = (1200000)
horasExtra = int(input("Ingrese las cantidad de horas extras:"))
totalSalario = 0
if horasExtra>0:
    totalSalario = horasExtra+0.50*salario
    print("mas las horas extras su salario sera de $",salario+totalSalario)