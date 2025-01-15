print("Bem-vindo a calculadora de aumento de 15% salário!\n")

salario = float(input("Digite o salário do funcionário: "))

aumento = salario + (salario * 15 / 100)

print("O funcionário que recebia R${:.2f}, com 15% de aumento, passa a receber agora R${:.2f}".format (salario, aumento))