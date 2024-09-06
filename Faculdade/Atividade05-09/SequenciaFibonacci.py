n = int(input())  # Quantos fibonaccis o usuário quer

fibonaccis = []
if n == 1:
    fibonaccis.append(0)
elif n == 2:
    fibonaccis.append(0)
    fibonaccis.append(1)
elif n > 2:
    x = 1
    fibonaccis.append(0)
    fibonaccis.append(1)
    for i in range(0, n - 2):
        soma = fibonaccis[x] + fibonaccis[x - 1]
        fibonaccis.append(soma)
        x += 1

#   map - percorrendo por todos valores contidos em fibonaccis e aplicando str() nesses mesmos valores.
''' fibonaccis = ' '.join - agora que fibonaccis tornou-se um array de strings ([x, y, z]); o metodo join substitui une os valores tornando-se [xyz],
    entretando, como usei ' ' junto ao metodo join, entre os valores unidos será colocado o valor que eu digitei. (' ') ou seja, deixando um espaço em branco.
'''
#   dessa maneira, o que antes era o array fibonaccis agora é uma variavel string, e seus valores é igual a todos valores de array fibonaccis em formato string,
#   separado por espaços em branco agora
fibonaccis = ' '.join(map(str, fibonaccis))
print(fibonaccis)
