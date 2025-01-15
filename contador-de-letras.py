frase = str(input("Digite uma frase: ")).lower().strip()

l = frase.count('a')
p = frase.find('a') + 1
u = frase.rfind('a') + 1

print("\nA letra A aparece {} vezes na frase".format(l))
print("A primeira letra A  apareceu na posição {}".format(p))
print("A última letra A apareceu na posição {}".format(u))