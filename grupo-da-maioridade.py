from datetime import date

print("Bem-vindo ao programa de grupo da maioridade!\n")

anoatual = date.today().year
contador = 0
contador2 = 0

for anos in range(1, 8):
    nascimento = int(input("Em que ano a {}ª pessoa nasceu? ".format(anos)))
    idade = anoatual - nascimento
    if idade >= 18:
        contador += 1
    else:
        contador2 += 1

print("\nAo todo tivemos {} pessoas maiores de idade".format(contador))
print("E também tivemos {} pessoas menores de idade".format(contador2))