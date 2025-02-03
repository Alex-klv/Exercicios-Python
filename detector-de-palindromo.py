print("Bem-vindo ao programa de identificação se a frase é palíndromo ou não.\n")
frase = str(input("Digite uma frase: ")).strip().upper()
fatiamento = frase.split()
junto = ''.join(fatiamento)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print("\nO inverso de {} é {}".format(junto, inverso))
    print("Temos um palíndromo!")
else:
    print("\nO inverso de {} é {}".format(junto, inverso))
    print("A frase digitada não é um palíndromo!")