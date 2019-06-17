# Faca um Programa que peca dois numeros e imprima a soma.

# a funcao input aceita somente numeros
a = input("Informe o valor de A: ")

# a funcao raw_input aceita strings
b = input("Informe o valor de B: ")

# int(variavel) Converte para inteiro
# str(variavel) Converte para string

# A soma de A + B = VALOR
resultado = float(a) + float(b)

# Tipos de formatacoes:
# %d inteiros
# %s strings
# %f float (decimais)
# %0.2 formata o valor de float para usar 2 casas decimais

# forma primitiva de concatenacao
# print("A soma de " + a + " + " + b + " = " + str(resultado))

# Forma mais eficiente para concatenar strings com inteiros
# print("A soma de %s + %s = %d" % (a, b, resultado))

# Exemplo de formatacao para numeros decimais (float)
print("A soma de %s + %s = %0.2f" % (a, b, resultado))

