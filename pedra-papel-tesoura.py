from random import randint
from time import sleep

print("""Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

jogada = int(input("Qual é a sua jogada? "))

print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!\n")

lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('=-=' * 15)
print("O jogador jogou {}".format(lista[jogada]))
print("Computador jogou {}".format(lista[computador]))
print('=-=' * 15)
if computador == 0:
    if jogada == 0:
        print("\nA jogada deu empate.")
    elif jogada == 1:
        print("\nO jogador ganhou!")
    elif jogada == 2:
        print("\nO computador ganhou!")
    else:
        print("\nJogada inválida")

elif computador == 1:
    if jogada == 0:
        print("\nComputador ganhou!")
    elif jogada == 1:
        print("\nA jogada deu empate.")
    elif jogada == 2:
        print("\nJogador ganhou!")
    else:
        print("\nJogada inválida")

elif computador == 2:
    if jogada == 0:
        print("\nJogador ganhou!")
    elif jogada == 1:
        print("\nComputador ganhou!")
    elif jogada == 2:
        print("\nA jogada deu empate.")
    else:
        print("\nJogada inválida")