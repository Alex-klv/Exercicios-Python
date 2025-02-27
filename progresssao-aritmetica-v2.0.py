print("Bem-vindo ao gerador de PA")
print("=-="*15)

pt = int(input("Primeiro termo: "))
rpa = int(input("Razão da PA: "))
termo = pt
contador = 1

while contador <= 10:
    print("{}".format(termo), end=' -> ')
    termo += rpa
    contador += 1
print("FIM")