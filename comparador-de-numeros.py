print("Bem-vindo ao programa que compara números\n")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("\nO primeiro valor é maior!")

elif n2 > n1:
    print("\nO segundo valor é maior!")

else:
    print("\nOs dois números são iguais!")