while True:
    try:
        idade = int(input("digite sua idade: "))
        idade2 = idade
        if idade + idade2 == idade * 2:
            break
    except ValueError:
        print("Digite apenas números!") 
#   Não permite o código quebrar se não digitar números para a idade,
#   nem mesmo prosseguir se não fizer o mesmo. (while loop)
#   =================================================================
    
minha_idade = 19
print(f"\nsua idade é: {idade} anos, e a minha idade é {minha_idade} anos.")

variavel = int()
variavel2 = float()
variavel3 = '3.85'
variavel4 = 'a' # 'Char'
variavel5 = str()
variavel6 = bool()


print(f"Inteiro: {variavel}")
print(f"Ponto flutuante: {variavel2:.2f}") # :.2f para 2 decimais 
print(f"Decimal {variavel3}")
print(f"Caractere: '{variavel4}'") # Boa pratica referenciar char com aspas simples ''.
print(f"String vazia: '{variavel5}'")
print(f"Booleano: {variavel6}")



# TIPOS DE VARIÁVEIS
  # inteira - armazenar os numeros inteiros (int)
  # ponto flutuante - armazenar os numeros decimais menores (float)
  # décimo - armazenar os numeros decimais maiores (double)
  # letra - armazenar os caracteres com base na tabela ASCII (char)
  # nome - armazena uma sequencia de caracteres(str)
  # boleana - armazena a dualidade - verdadeira ou falsa (bool)