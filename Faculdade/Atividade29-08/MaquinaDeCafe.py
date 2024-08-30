andar1 = int(input())
andar2 = int(input())
andar3 = int(input())

while andar1 < 0 or andar2 < 0 or andar3 < 0:
    andar1 = int(input())
    andar2 = int(input())
    andar3 = int(input())
if andar1 > 1000:
    andar1 = 1000
if andar2 > 1000:
    andar2 = 1000
if andar3 > 1000:
    andar3 = 1000
#   Não permite mais de 1000
#   Funcionários por andar

tempoGasto = andar1 + andar3
print(tempoGasto * 2)