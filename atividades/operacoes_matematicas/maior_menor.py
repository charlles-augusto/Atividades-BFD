# Script: Maior e Menor Valor
# Descrição: Programa que lê vários números inteiros em uma única linha e encontra o maior e menor valor
# Conceito: Processamento de listas e uso de funções built-in max() e min()
# Autor: Desenvolvedor Python
# Data: 2024

# Entrada de dados - Lê números inteiros em uma única linha
# input() captura a linha completa como string
# .split() divide a string em uma lista usando espaços como delimitadores
# List comprehension [int(num) for num in numbers] converte cada elemento para inteiro
numbers = input("Digite inteiros separados por espaços: ").split()
numbers = [int(num) for num in numbers]

# Processamento - Encontra o maior e menor valor
# max() retorna o maior elemento da lista
# min() retorna o menor elemento da lista
max_value = max(numbers)
min_value = min(numbers)

# Saída de dados - Exibe os resultados formatados
# f-strings incluem os valores calculados nas mensagens
print(f"O maior valor é: {max_value}")
print(f"O menor valor é: {min_value}")

# Informações adicionais:
print(f"\nEstatísticas completas:")
print(f"Quantidade de números: {len(numbers)}")
print(f"Números digitados: {numbers}")
print(f"Amplitude (max - min): {max_value - min_value}")

# Observações sobre o código:
# - Esta abordagem é mais eficiente que loops manuais
# - List comprehension é mais pythonica e legível
# - Não há validação de entrada - números inválidos causarão erro
# - Para maior robustez, poderia usar try-except na conversão
# - Alternativa manual sem max/min:
#   max_val = numbers[0]
#   min_val = numbers[0]
#   for num in numbers[1:]:
#       if num > max_val: max_val = num
#       if num < min_val: min_val = num
