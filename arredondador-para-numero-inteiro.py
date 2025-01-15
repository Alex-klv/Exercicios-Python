from math import trunc
print("Bem-vindo ao programa que arredonda um numero sem ser inteiro para inteiro\n")

num = float(input("Digite um numero: "))
por = trunc(num)

print("O valor digitado foi {} e seu valor inteiro é {}".format(num, por))