maior = menor = soma = quantidade = produtomaior = 0
produtomenor = ''

while True:
    print("---"*10)
    print("LOJA SUPER BOM".center(30))
    print("---"*10)

    produto = str(input("Nome do Produto: ")).strip()
    preço = float(input("Preço: R$"))

    soma += preço
    quantidade += 1

    if preço > 1000:
        produtomaior += 1

    if quantidade == 1 or preço < menor:
        menor = preço
        produtomenor = produto

    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

print("---"*10)
print("FIM DO PROGRAMA".center(30))
print("---"*10)

print(f"O total da compra foi de R${soma:.2f}")
print(f"temos {produtomaior} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {produtomenor} que custa R${menor:.2f}")