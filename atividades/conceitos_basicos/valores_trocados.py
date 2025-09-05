# Script: valores_trocados.py
# Descrição: Demonstra como trocar valores entre duas variáveis
# Objetivo: Ensinar o conceito de troca de valores usando variável temporária

# Entrada de dados: solicita dois valores inteiros ao usuário
# A função int() converte a string retornada por input() para número inteiro

# Solicita o primeiro valor inteiro e armazena na variável 'a'
print("=== Programa de Troca de Valores ===")
a = int(input("Digite o valor de a: "))

# Solicita o segundo valor inteiro e armazena na variável 'b'
b = int(input("Digite o valor de b: "))

# Exibe os valores originais para referência
# O \n adiciona uma quebra de linha para melhor formatação
print(f"\nValores originais: a = {a}, b = {b}")

# Processo de troca de valores entre variáveis
# Este é um algoritmo clássico de troca usando variável temporária

# Passo 1: Armazena o valor de 'a' em uma variável temporária
# Isso evita a perda do valor original de 'a' durante a troca
temp = a  # temp agora guarda o valor original de 'a'

# Passo 2: Atribui o valor de 'b' para 'a'
# Agora 'a' possui o valor original de 'b'
a = b  # 'a' recebe o valor que estava em 'b'

# Passo 3: Atribui o valor da variável temporária para 'b'
# 'b' recebe o valor original de 'a' que estava guardado em temp
b = temp  # 'b' recebe o valor original de 'a'

# Exibe os valores após a troca
# Note que agora as variáveis contêm valores trocados
print(f"Valores trocados: a = {a}, b = {b}")

# Explicação adicional:
# Este método é conhecido como "troca com variável temporária"
# É o método mais simples e seguro para trocar valores entre duas variáveis
