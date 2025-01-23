print("============= SUPERMECADO =============\n")
preço = float(input("Digite o preço das compras: R$ "))
print("""FORMAS DE PAGAMENTO\n
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opçao = int(input("\nQual é a opção? "))

if opçao == 1:
    p1 = (preço * 10) / 100
    t1 = preço - p1
    print("\nSua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, t1))

elif opçao == 2:
    p2 = (preço * 5) / 100
    t2 = preço - p2
    print("\nSua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, t2))

elif opçao == 3:
    p3 = preço / 2
    print("\nSua compra parcelada em 2x fica R${:.2f} sua compra sem parcelas é R${:.2f}".format(p3, preço))

elif opçao == 4:
    parcelamento = int(input("Quantas parcelas? "))
    p4 = (preço * 20) / 100
    t4 = p4 + preço
    x = t4 / parcelamento
    print("\nSua compra parcelada em {}x fica R${:.2f} com JUROS".format(parcelamento, x))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, t4))

elif opçao != 1 or opçao != 2 or opçao != 3 or opçao != 4:
    print("\nDigite uma alternativa correta.")
    exit()