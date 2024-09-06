# Lê o valor de N (neste caso, ele nem é usado diretamente)
N = int(input())

# Lê os números da segunda linha e converte cada um deles para inteiro
numeros = [int(x) for x in input().split()]

# Calcula a soma dos números
soma = sum(numeros)

# Exibe o resultado
print(soma)
