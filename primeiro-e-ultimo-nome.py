nome = str(input("Digite o seu nome completo: ")).strip()

n = nome.split()

p = n[0]
u = n[len(n)-1]

print("Seu primeiro nome é {}".format(p))
print("Seu ultimo nome é {}".format(u))