print("Bem-vindo ao caixa eletrônico.")

print("""
    [1] - Consultar saldo
    [2] - Sacar
    [3] - Depositar
    [4] - Sair""")

opçao = int(input("\nDigite uma opção: "))

if opçao == 1:
    print("\nSeu saldo atual é de R$ 5000")

elif opçao == 2:
    saque = float(input("Qual o valor do saque: "))
    if saque >= 5001:
        print("\nSaldo insuficiente, tente novamente!")
    elif saque <= 5000:
        t = 5000 - saque
        print(f"\nVocê sacou R${saque:.2f} e restou na sua conta R${t:.2f}.")

elif opçao == 3:
    deposito = float(input("\nDigite o valor de depósito para sua conta: "))
    soma = deposito + 5000
    print(f"\nSeu saldo atual na sua conta é de R${soma:.2f}")

elif opçao == 4:
    print("\nObrigado por consultar sua conta volte sempre!")

else:
    print("\nOpção invalida selecione uma opção valida.")