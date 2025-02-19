from time import sleep
pv = int(input("Digite o primeiro valor: "))
sv = int(input("Digite o segundo valor: "))
op = 0
while op != 5:
    print("""    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    op = int(input("Qual é a sua opção? "))
    if op == 1:
        soma = pv + sv
        print("A soma entre {} + {} é {}.".format(pv, sv, soma))
        print('=-='*20)
    elif op == 2:
        mult = pv * sv
        print("O resultado de {} x {} é {}".format(pv, sv, mult))
        print('=-='*20)
    elif op == 3:
        if pv > sv:
            print("Entre {} e {} o maior valor é {}".format(pv, sv, pv))
            print('=-='*20)
        else:
            print("Entre {} e {} o maior valor é {}".format(pv, sv, sv))
            print('=-='*20)
    elif op == 4:
        print("Informe os números novamente: ")
        pv = int(input("Primeiro valor: "))
        sv = int(input("Segundo valor: "))
        print('=-='*20)
print("Finalizando...")
print("=-="*20)
sleep(2)
print("Fim do programa! Volte sempre!")