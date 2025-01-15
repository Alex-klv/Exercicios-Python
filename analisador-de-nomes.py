print("Bem-vindo ao analisador de nomes!\n")

nome = str(input("Digite seu nome completo: "))
print("Estamos analisando o seu nome...\n")

Mnome = nome.upper()
mnome = nome.lower()

stripnome = nome.strip()
lennome = len(stripnome) - nome.count(" ")

splitnome = nome.split()
fatianome = splitnome[0]
contnome = len(fatianome)

print("Seu nome em maiúsculo é {}".format(Mnome))
print("Seu nome em minúsculo é {}".format(mnome))
print("Seu nome ao todo tem {} letras".format(lennome))
print("Seu primeiro nome é {} e ele tem {} letras".format(fatianome, contnome))