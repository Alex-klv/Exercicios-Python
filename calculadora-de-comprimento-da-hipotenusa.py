from math import hypot

print("Bem-vindo ao programa que calcula o comprimento da hipotenusa.\n")

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot (co, ca)

print("O resultado do comprimento da hipotenusa é {:.2f}".format(hi))