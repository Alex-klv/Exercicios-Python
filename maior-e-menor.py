print("Bem-vindo ao programa de valores maiores e menores.\n")

primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))
terceiro = int(input("Terceiro valor: "))

if primeiro > segundo and primeiro > terceiro:
    maior = primeiro

if segundo > primeiro and segundo > terceiro:
    maior = segundo

if terceiro > primeiro and terceiro > segundo:
    maior = terceiro


if primeiro < segundo and primeiro < terceiro:
    menor = primeiro

if segundo < primeiro and segundo < terceiro:
    menor = segundo

if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

print("\nO número maior é {}".format(maior))
print("O número menor é {}".format(menor))