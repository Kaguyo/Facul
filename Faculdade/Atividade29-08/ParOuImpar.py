BinoPar = int(input())
CinoImpar = int(input())

if BinoPar > 10:
    BinoPar = 10
#   ====
if CinoImpar > 10:
    CinoImpar = 10

Soma = BinoPar + CinoImpar
if Soma % 2 != 0:
    print("Cino")
else:
    print("Bino")