print("Bem-vindo a calculadora de desconto!\n")

preco = float(input("Digite o preço da sua compra R$ "))

total =  preco - (preco * 5 / 100)

print("O produto custava R${}, com a promoção de 5% vai custar R${}.".format (preco, total))