n = int(input())
array = []
fibonaccis = 0
copia_fibonacci = 1

for i in range(n):
    array.append(fibonaccis)
    fibonaccis, copia_fibonacci = copia_fibonacci, fibonaccis + copia_fibonacci

# Converte cada número para string e imprime sem vírgulas
print(' '.join(map(str, array)))
