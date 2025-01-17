print("Bem-vindo ao programa de calculo de aumento de salário!\n")

salario = float(input("Digite o seu sálario: "))

if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
    print("\nSeu salário era R${:.2f} e agora com o aumento de 15% ficou R${:.2f}".format(salario, aumento))

else:
    aumentomaior = salario + (salario * 10 / 100)
    print("\nSeu salário era R${:.2f} e agora com o aumento de 10% ficou R${:.2f}".format(salario, aumentomaior))