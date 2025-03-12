resposta = 'S'
quantidade = soma = media = maior = menor = 0
while resposta in 'Ss':
    n = int(input("Digite um número: "))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

media = soma / quantidade
print("\nVocê digitou {} números e a média deles foram {:.2f}".format(quantidade, media))
print("O maior valor foi de {} e o menor foi {}".format(maior, menor))