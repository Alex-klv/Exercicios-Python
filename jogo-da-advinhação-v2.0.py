from random import choice

print("\033[34m=-=\033[0m"*30)
print("\033[32mBem-vindo ao jogo de adivinhação v2.0! Adivinhe um número que escolhi entre 0 e 10.\033[0m")
print("\033[34m=-=\033[0m"*30)

numero = int(input("\nQual número eu pensei? "))

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = choice(lista)

while resultado != numero:
    if resultado > numero:
        numero = int(input("O número é maior, tente novamente: "))
    else:
        numero = int(input("O número é menor, tente novamente: "))

print("Parabêns você acertou o número correto é {}".format(resultado))