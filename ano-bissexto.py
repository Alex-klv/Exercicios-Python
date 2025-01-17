from datetime import date

print("Bem-vindo ao programa para saber se o ano é bisseto ou saber analisar o seu ano atual!\n")
ano = int(input("Coloque o ano que deseja ou digite 0 para saber qual ano você está agora: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é bissexto".format(ano))

else:
    print("O ano {} não é bissexto".format(ano))