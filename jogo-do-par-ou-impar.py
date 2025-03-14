from random import randint
cont = 0
print("-=-"*20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-=-"*20)

while True:
    valor = int(input("Diga um valor: "))
    computador = randint(1, 10)
    soma = valor + computador
    opçao = ' '

    while opçao not in 'PI':
        opçao = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    print("~~~"*20)
    print(f"Você jogou {valor} e o computador {computador}. Total de {soma}", end='')
    print(" Deu PAR" if soma % 2 == 0 else " Deu ÍMPAR")
    print("~~~"*20)

    if opçao == 'P':
        if soma % 2 == 0:
            print("Você VENCEU!!!")
            cont += 1
        else:
            print("Você PERDEU!")
            print("-=-"*20)
            break
    elif opçao == 'I':
        if soma % 2 == 1:
            print("Você VENCEU!!!")
            cont += 1
        else:
            print("Você PERDEU!")
            print("-=-"*20)
            break
    print("Vamos jogar novamente....")
print(f"GAMEOVER! Você venceu {cont} vezes.")