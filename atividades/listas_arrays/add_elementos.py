# Script: add_elementos.py
# Descrição: Demonstra como criar uma lista vazia e adicionar elementos dinamicamente
# Objetivo: Ensinar o uso do método append() para construir listas iterativamente

# Inicialização de uma lista vazia
# A lista 'numeros' começa sem nenhum elemento
numeros = []

# Processo de coleta de dados
# Loop para coletar 5 números inteiros do usuário
# range(5) gera números de 0 a 4
for i in range(5):
    # Solicita um número inteiro ao usuário
    # i+1 ajusta a numeração para o usuário (1 a 5)
    num = int(input(f"Digite o número {i+1}: "))
    
    # Adiciona o número digitado à lista
    # append() adiciona o elemento ao final da lista existente
    numeros.append(num)
    
    # A cada iteração, a lista cresce:
    # Iteração 1: [num1]
    # Iteração 2: [num1, num2]
    # Iteração 3: [num1, num2, num3]
    # ... e assim por diante

# Exibição do resultado final
# Mostra a lista completa após adicionar todos os elementos
print("\n=== Lista Construída ===")
print("Lista completa:", numeros)

# Informações adicionais sobre a lista:
print(f"Total de elementos: {len(numeros)}")
print(f"Tipo de dados: {type(numeros)}")
print(f"Elementos em ordem: {numeros}")

# Observações:
# - append() sempre adiciona ao final da lista
# - A lista cresce dinamicamente conforme necessário
# - Os elementos mantêm a ordem em que foram adicionados
