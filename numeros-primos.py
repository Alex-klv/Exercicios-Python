print("Bem-vindo ao programa para saber se o numero é primo\n")
num = int(input("Digite um número: "))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[32m',end=' ')
        cont = cont + 1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c),end=' ')
print("\n\033[mO número {} foi divisível {} vezes".format(num, cont))
if cont == 2:
    print("Por isso ele é PRIMO!")
else:
    print("Por isso ele não é PRIMO!")