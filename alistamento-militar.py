from datetime import date

print("Bem-vindo ao programa do alistamento militar!\n")

nascimento = int(input("Digite seu ano de nascimento: "))

anoatual = date.today().year
idade = anoatual - nascimento

if idade > 18:
    passado = idade - 18
    anoatras = anoatual - passado
    print("Você nasceu em {} tem {} anos em {}.".format(nascimento, idade, anoatual))
    print("Você já deveria ter se alistado há {} anos.".format(passado))
    print("Seu alistamento foi em {}.".format(anoatras))
elif idade < 18:
    futuro = 18 - idade
    anofuturo = anoatual + futuro
    print("Você nasceu em {} tem {} anos em {}.".format(nascimento, idade, anoatual))
    print("Você deverá se alistar daqui há {} anos.".format(futuro))
    print("Seu alistamento será em {}.".format(anofuturo))
else:
    print("Você nasceu em {} tem {} anos em {}.".format(nascimento, idade, anoatual))
    print("Você deve se alistar IMEDIATAMENTE!")
