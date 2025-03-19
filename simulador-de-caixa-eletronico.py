print('~' * 30)
print('{:^30}'.format('BANCO DNO'))
print('~' * 30)

valor = int(input("Qual valor você quer sacar? R$ "))
total = valor
cedula = 100
totalcedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f"Total de {totalcedula} cédulas de R${cedula}")
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break 

print('~' * 30)
print('{:^30}'.format('Volte sempre ao BANCO DNO'))
print('~' * 30)