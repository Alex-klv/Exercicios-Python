print('=-=' * 15)
print("Bem-vindo ao analisador de trângulos!")
print('=-=' * 15)

a = float(input("\nPrimeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("\nOs segmentos acima podem forma um triângulo!")

else:
    print("\nOs segmentos acima não podem forma um triângulo!")