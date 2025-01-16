km = float(input("Qual a velocidade atual do carro? "))

if km <= 80:
    print("\nTenha um bom dia! Dirija com segurança.")
    exit()

else:
    multa = (km - 80) * 7

    print("\nMULTADO! Você passou do limite de velocidade permitido que é 80km/h")
    print("Você deve pagar uma multa de {:.2f}".format(multa))
    print("\nTenha um bom dia! Dirija com segurança.")
    exit()