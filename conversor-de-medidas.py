print("Bem vindo ao conversor de medidas!!\n")

metros = float(input("Digite a distancia em metros: "))

print("Sua medida de {}m corresponde a \n".format(metros))

km = metros / 1000
hm = metros / 100
dam = metros / 10
m = metros
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print("{} km".format(km))
print("{} hm".format(hm))
print("{} dam".format(dam))
print("{} m".format(metros))
print("{} dm".format(dm))
print("{} cm".format(cm))
print("{} mm".format(mm))