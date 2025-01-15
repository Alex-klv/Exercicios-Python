from random import choice

print("Bem-vindo ao programa de sorteio de qual aluno vai apresentar o trabalho primeiro.\n")

n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print("\nO aluno escolhido foi {}".format(escolhido))