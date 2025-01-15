from math import sin,cos,tan,radians

print("Bem-vindo ao que vai calcular o valor do seno, cosseno e tangente diacordo com o ângulo que desejar.\n")

angulo = float(input("Digite o ângulo que voce desejar: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O ângulo de {} tem o seno de {:.2f}".format(angulo, seno))
print("O ângulo de {} tem o cosseno de {:.2f}".format(angulo, cosseno))
print("O ângulo de {} tem o tangente de {:.2f}".format(angulo, tangente))