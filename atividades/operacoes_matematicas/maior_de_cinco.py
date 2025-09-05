# Script: Maior de Cinco Números
# Descrição: Programa que lê 5 números do usuário e identifica o maior valor
# Conceito: Algoritmo de busca do máximo em uma sequência
# Autor: Desenvolvedor Python
# Data: 2024

# 5. Escreva um programa que leia 5 números e mostre o maior deles.

# Inicialização da variável para armazenar o maior número
# Usa float('-inf') para garantir que qualquer número digitado será maior
# Esta técnica é conhecida como inicialização com infinito negativo
maior_numero = float('-inf')

# Processamento principal - Loop para ler e comparar 5 números
# range(5) gera os valores 0, 1, 2, 3, 4 (total de 5 iterações)
for i in range(5):
    try:
        # Entrada de dados com tratamento de exceções
        # f-string formata a mensagem com o número da posição (i+1 para começar do 1º)
        numero = float(input(f"Digite o {i+1}º número: "))
        
        # Lógica de comparação - Atualização do máximo
        # Compara cada novo número com o maior encontrado até agora
        if numero > maior_numero:
            # Atualiza o maior número encontrado
            maior_numero = numero
            # Observação: Esta é uma técnica eficiente de O(n) para encontrar o máximo
    except ValueError:
        # Tratamento de erro para entrada inválida
        # Se o usuário digitar algo que não seja número, exibe mensagem de erro
        # Nota: O programa continua pedindo os 5 números mesmo após erro
        print("Entrada inválida. Por favor, digite um número.")

# Saída de dados - Exibe o resultado final
# f-string formata a mensagem com o valor encontrado
print(f"O maior número digitado é: {maior_numero}")

# Análise de complexidade:
# - Tempo: O(n) onde n=5 (linear)
# - Espaço: O(1) (constante, usa apenas uma variável extra)

# Alternativas possíveis:
# - Armazenar todos os números em uma lista e usar max(lista)
# - Usar sorted() para ordenar e pegar o último elemento
# - Versão com lista: numbers = [float(input()) for _ in range(5)]; max(numbers)