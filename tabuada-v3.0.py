while True:
    print("Digite um número negativo para parar.")
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("-=-"*25)
    if n < 0:
        break
    for c in range (1, 11):
        print(f"{n} x {c} = {n*c}")
    print("-=-"*25)
print("Programa tabuada encerrado. Volte sempre!")