from random import choice
from time import sleep

print("\033[33m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m")
print("\033[34mBem-vindo ao jogo! Adivinhe o número que escolhi entre 0 e 5.\033[0m")
print("\033[33m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m\n")

numero = int(input("Qual número eu pensei? "))

if numero > 5:
    print("\nDigite o número de 0 a 5 corretamente.")
    exit()

print("\033[30mPROCESSANDO...\033[0m")

sleep(2)

lista = [0, 1, 2, 3, 4, 5]
resultado = choice(lista)

if resultado == numero:
    print("\033[32mParabêns você acertou!\033[0m")

else:
    print("\033[31mVocê errou tente novamente.\033[0m")