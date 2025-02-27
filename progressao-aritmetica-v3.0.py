print("Bem-vindo ao gerador de PA")
print("=-="*15)

pt = int(input("Primeiro termo: "))
rpa = int(input("Razão da PA: "))

termo = pt
contador = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print("{}".format(termo), end=' -> ')
        termo += rpa
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados.".format(total))
print("FIM")