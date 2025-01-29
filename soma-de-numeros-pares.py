print("Bem-vindo a calculadora de soma de números pares!\n")
contador = 0
soma = 0
for c in range(1, 7):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        contador = contador + 1
        soma = soma + numero
print("\nVocê informou {} números a pares a soma dos números pares foi {}.".format(contador, soma))