NotaA, NotaB = map(float, input().split())


if NotaA > 10:
    NotaA = 10
if NotaB > 10:
    NotaB = 10

Sumario = NotaA + NotaB

if Sumario / 2 >= 7:
    print("Aprovado")
elif Sumario / 2 >= 4 and Sumario / 2 < 7:
    print("Recuperacao")
else:
    print("Reprovado")