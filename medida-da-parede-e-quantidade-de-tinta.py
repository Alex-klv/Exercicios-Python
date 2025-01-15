L = float(input("Digite a largura da parede: "))
A = float(input("Digite a altura da parede: "))

dimensao = L * A
tinta = dimensao / 2

print("Sua parede tem a dimensão de {} x {} e sua área é de {}m².".format(L, A, dimensao))
print("Para pintar essa parede, vocé precisará de {}L de tinta.".format(tinta))