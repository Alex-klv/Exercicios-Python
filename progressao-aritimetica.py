print('==='* 10)
print("      10 TERMOS DE UMA PA   ")
print('==='* 10)

pa = int(input("\nPrimeiro termo: "))
rz = int(input("Razão: "))
decimo = pa + (10 - 1)  * rz

for c in range(pa, decimo + rz, rz):
    print('{}'.format(c), end= ' -> ')
print("FIM")