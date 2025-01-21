print("Bem-vindo ao programa de aprovamento de emprestimo!\n")

casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário do comprador: "))
anos = int(input("Digite quantos anos de financiamento: "))

meses = 12 * anos
parcelas = casa / meses
porcen = (salario * 30 / 100)

if parcelas <= porcen:
    print("\nPara pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.".format(casa, anos, parcelas))
    print("Empréstimo CONCEDIDO!")

else:
    print("\nPara pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.".format(casa, anos, parcelas))
    print("Empréstimo NEGADO!")