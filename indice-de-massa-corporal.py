print("Bem-vindo ao programa para saber seu IMC.\n")

peso = float(input("Digite seu peso em (KG): "))
altura = float(input("Digite sua altura em (M): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("\nO IMC dessa pessoa está em {:.1f}".format(imc))
    print("Você está ABAIXO do peso, CUIDADO!")

elif imc >= 18.5 and imc < 25:
    print("\nO IMC dessa pessoa está em {:.1f}".format(imc))
    print("Parabens, você está no PESO NORMAL!")

elif imc >= 25 and imc < 30:
    print("\nO IMC dessa pessoa está em {:.1f}".format(imc))
    print("Você está em SOBREPESO.")

elif imc >= 30 and imc < 40:
    print("\nO IMC dessa pessoa está em {:.1f}".format(imc))
    print("Você está nível de OBESIDADE, CUIDADO!")

else:
    print("\nO IMC dessa pessoa está em {:.1f}".format(imc))
    print("Você está em OBESIDADE MORBIDA, procure um médico imediatamente!")