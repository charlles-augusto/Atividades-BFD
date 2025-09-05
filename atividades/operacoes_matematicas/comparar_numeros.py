# Script: Comparar Números
# Descrição: Programa que compara dois números inteiros e informa qual é maior, menor ou se são iguais
# Autor: Desenvolvedor Python
# Data: 2024

# Entrada de dados - Solicita dois números inteiros ao usuário
# A função int() converte a entrada string para número inteiro
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

# Processamento e decisão - Compara os números usando estrutura condicional
# Verifica três possibilidades: maior, menor ou igual
if num1 > num2:
    # Caso 1: Primeiro número é maior que o segundo
    print(f"{num1} é maior que {num2}")
elif num1 < num2:
    # Caso 2: Primeiro número é menor que o segundo
    print(f"{num1} é menor que {num2}")
else:
    # Caso 3: Os números são iguais
    print(f"{num1} é igual a {num2}")

# Observações:
# - O programa usa estrutura condicional if-elif-else para cobrir todas as possibilidades
# - f-strings são usadas para formatar a saída de forma clara
# - Não há validação de entrada, assume que o usuário digitará números válidos
