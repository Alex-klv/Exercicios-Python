print('-=-'* 10)
print("Bem-vindo a tabuada 2.0!")
print('-=-'* 10)
numero = int(input("\nDigite um numero para ver a sua tabuada: "))
for mult in range (1, 11):
    result = mult * numero
    print("{} X {} = {}".format(numero, mult, result))