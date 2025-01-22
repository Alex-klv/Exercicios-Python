print("Bem-vindo ao programa de notas!\n")
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2

if media >= 7.0:
    print("Quem tirou {} e {} a média do aluno é {}".format(n1, n2, media))
    print("O aluno está APROVADO!")

elif media >= 5.0 and media < 6.9:
    print("Quem tirou {} e {} a média do aluno é {}".format(n1, n2, media))
    print("O aluno está em RECUPERAÇÃO!")

elif media <= 4.9:
    print("Quem tirou {} e {} a média do aluno é {}".format(n1, n2, media))
    print("O aluno está REPROVADO!")

else:
    print("Digite a sua nota novamente!")
    exit()