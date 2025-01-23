print("=-=" * 15)
print("Bem-vindo ao analisador de triângulos!")
print("=-=" * 15)

a = float(input("\nPrimeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("\nOs segmentos acima podem forma um triângulo ", end = '')

    if a != b != c != a:
        print("ESCALENO!")
    elif a == b == c:
        print("EQUILÁTERO!")
    else:
        print("ISÓSCELES!")
else:
    print("Os segmentos acima NÃO podem forma um triângulo.")