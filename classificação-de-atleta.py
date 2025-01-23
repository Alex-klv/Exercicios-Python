from datetime import date

print("Bem-vindo ao programa para saber a sua classificação de atleta!\n")

ano = int(input("Digite o seu ano de nascimento: "))

anoatual = date.today().year
idade = anoatual - ano


if idade <= 9:
    print("\nO atleta tem {} anos".format(idade))
    print("Classificação: MIRIM")

elif idade >= 14 and idade < 19:
    print("\nO atleta tem {} anos".format(idade))
    print("Classificação: INFANTIL")

elif idade >= 19 and idade < 25:
    print("\nO atleta tem {} anos".format(idade))
    print("Classificação: JÚNIOR")

elif idade == 25:
    print("\nO atleta tem {} anos".format(idade))
    print("Classificação: SÊNIOR")

elif idade > 25:
    print("\nO atleta tem {} anos".format(idade))
    print("Classificação: MASTER")