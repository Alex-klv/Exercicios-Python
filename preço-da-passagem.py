print("Bem-vindo ao programa para saber o custo da sua viagem!\n")

km = float(input("Digite qual é a distancia da sua viagem: "))

if km <= 200:
    d = float(km * 0.50)
    print("Você está prestes a começar a sua viagem de {}Km".format(km))
    print("E o preço da sua passagem será de R${:.2f}".format(d))

else:
    u = float(km * 0.45)
    print("Você está  prestes a começar a sua viagem ded {}Km".format(km))
    print("E o preço da sua passagem será de R${:.2f}".format(u))