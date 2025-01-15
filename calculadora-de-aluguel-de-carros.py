print("Bem-vindo a calculadora de aluguel de carros!\n")

dias = int(input("Digite quantos dias alugados?: "))
km = float(input("Digite quantos Km rodados?: "))
pago = dias * 60
andado = km * 0.15
total = pago + andado

print("O total a pagar é R${:.2f}".format(total))