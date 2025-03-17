dezoitoanos = feminino = masculino = idademulher = 0

while True:
    print("---"*10)
    print("CADASTRE UMA PESSOA".center(30))
    print("---"*10)

    idade = int(input("Idade: "))

    if idade >= 18:
        dezoitoanos += 1
    sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]

    if sexo == 'M':
        masculino += 1
    elif sexo == 'F':
        feminino += 1
        if idade < 20:
            idademulher += 1
    else:
        print("Digite uma das 2 opções.")
    print("---"*10)

    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    
    if continuar == 'N':
        break
    else:
        continue
print(f"Total de pessoas com mais de 18 anos: {dezoitoanos}")
print(f"Ao todo temos {masculino} homens cadastrados")
print(f"E temos {idademulher} mulheres com menos de 20 anos")