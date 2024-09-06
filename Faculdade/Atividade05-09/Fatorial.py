entrada = (int(input()))
copia_entrada =  entrada

if entrada == 0:
    copia_entrada = 1
else:
    for i in range(1, entrada):
        entrada = entrada -1
        entrada * entrada
        copia_entrada *= entrada

print(copia_entrada)