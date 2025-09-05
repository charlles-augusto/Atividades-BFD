# Script: lista_laco.py
# Descrição: Coleta todos os números pares dentro de um intervalo definido
# Objetivo: Demonstrar uso de loop com condição para filtrar números pares

# Entrada do usuário
# Solicita um número inteiro positivo que define o limite superior do intervalo
n = int(input("Digite um número N: "))

# Inicialização da lista para armazenar números pares
# Começa vazia e será preenchida durante o processamento
even_numbers = []

# Processamento dos números
# Loop que percorre todos os números de 1 até N (inclusive)
# range(1, n + 1) gera números de 1 até n (o +1 inclui n no intervalo)
for i in range(1, n + 1):
    # Verificação se o número é par
    # O operador % retorna o resto da divisão
    # Se i % 2 == 0, significa que i é divisível por 2 (número par)
    if i % 2 == 0:
        # Número par encontrado: adiciona à lista
        # append() insere o número no final da lista
        even_numbers.append(i)
        
        # Exemplo de execução:
        # Se n = 10, o loop processará: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        # Números pares: 2, 4, 6, 8, 10

# Exibição dos resultados
# Mostra todos os números pares encontrados no intervalo
print(f"Números pares de 1 até {n}: {even_numbers}")

# Informações adicionais sobre o resultado:
print(f"Total de números pares encontrados: {len(even_numbers)}")

# Observações sobre o algoritmo:
# - A verificação i % 2 == 0 é a forma mais comum de identificar números pares
# - A lista mantém a ordem crescente dos números
# - Este método é eficiente para intervalos pequenos a médios
