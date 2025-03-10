print("-=-"*10)
print("Sequência de Fibonacci")
print("=-="*10)

termos = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
t3 = 0
cont = 0
print("=-="*10)
while cont < termos:
    print("{} -> ".format(t3), end='')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    cont += 1
print("FIM")