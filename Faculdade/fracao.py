from fractions import Fraction

def operacao_frações(numerador1, denominador1, numerador2, denominador2, operacao):
    # Cria as frações a partir dos numeradores e denominadores
    frac1 = Fraction(numerador1, denominador1)
    frac2 = Fraction(numerador2, denominador2)
    
    # Realiza a operação desejada
    if operacao == '+':
        resultado = frac1 + frac2
    elif operacao == '-':
        resultado = frac1 - frac2
    elif operacao == '*':
        resultado = frac1 * frac2
    elif operacao == '/':
        resultado = frac1 / frac2
    else:
        raise ValueError("Operação inválida")
    
    return resultado

# Entrada dos valores
numerador1 = int(input("Digite o numerador da primeira fração: "))
denominador1 = int(input("Digite o denominador da primeira fração: "))
numerador2 = int(input("Digite o numerador da segunda fração: "))
denominador2 = int(input("Digite o denominador da segunda fração: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Restrições
if not (-1 < numerador1 < 102 and -1 < denominador1 < 102 and -1 < numerador2 < 102 and -1 < denominador2 < 102):
    print("Os números devem ser maiores que -1 e menores que 102.")
else:
    resultado = operacao_frações(numerador1, denominador1, numerador2, denominador2, operacao)
    print(f"Resultado: {resultado.numerator}/{resultado.denominator}")