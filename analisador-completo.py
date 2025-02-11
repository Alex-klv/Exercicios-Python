print("Bem-vindo ao analisador completo!\n")
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
contmulher = 0
for analisador in range(1, 5):
    print("----- {}ª PESSOA -----".format(analisador))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    somaidade += idade
    mediaidade = somaidade / 4
    if analisador == 1 and sexo == 'M':
        nomemaisvelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'F' and idade < 20:
        contmulher += 1
print("-"*21)
print("\nA média de idade do grupo é de {} anos.".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadehomem, nomemaisvelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(contmulher))