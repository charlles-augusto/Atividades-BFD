# Script: Intercalação de Duas Listas
# Descrição: Programa que lê duas listas de 10 números inteiros cada e cria uma terceira lista intercalando os elementos
# Conceito: Manipulação de listas, loops, entrada de dados e algoritmos de intercalação
# Autor: Desenvolvedor Python
# Data: 2024

# Inicialização das listas vazias
# A e B armazenarão os números digitados pelo usuário
# C armazenará o resultado da intercalação
A = []  # Lista A - armazenará 10 números inteiros
B = []  # Lista B - armazenará outros 10 números inteiros

# Entrada de dados - Coleta números para a lista A
# range(10) gera valores de 0 a 9 (total de 10 iterações)
print("Digite 10 números inteiros para a lista A:")
for i in range(10):
    # f-string formata a mensagem com a posição correta (i+1 para começar do 1º)
    num = int(input(f'Digite o {i+1}º número inteiro para lista A: '))
    # append() adiciona o número ao final da lista A
    A.append(num)

# Entrada de dados - Coleta números para a lista B
# Processo idêntico ao da lista A, mas para a segunda lista
print("\nDigite 10 números inteiros para a lista B:")
for i in range(10):
    num = int(input(f'Digite o {i+1}º número inteiro para lista B: '))
    B.append(num)

# Processamento - Criação da lista intercalada
# C conterá elementos de A e B em ordem alternada: A[0], B[0], A[1], B[1], ...
C = []  # Lista resultante vazia

# Método 1: Intercalação manual usando loop
# Este método é mais didático e mostra o processo passo a passo
for i in range(10):
    # Adiciona elemento da lista A na posição i
    C.append(A[i])  # Adiciona elemento da lista A
    # Adiciona elemento correspondente da lista B na mesma posição i
    C.append(B[i])  # Adiciona elemento da lista B
    # Resultado: C = [A[0], B[0], A[1], B[1], A[2], B[2], ...]

# Saída de dados - Exibição dos resultados
# Mostra as três listas para comparação visual
print("\nLista A:", A)
print("Lista B:", B)
print("Lista C (intercalada):", C)

# Informações adicionais sobre a intercalação
print(f"\nEstatísticas:")
print(f"Tamanho da lista A: {len(A)} elementos")
print(f"Tamanho da lista B: {len(B)} elementos")
print(f"Tamanho da lista C intercalada: {len(C)} elementos")

# Método 2 (alternativo): Usando insert - Comentado para referência
# Este método é menos eficiente (O(n²)) mas demonstra outra abordagem
'''
C = A.copy()  # Começa com uma cópia da lista A
for i in range(len(B)):
    # Insert insere B[i] na posição (i*2+1) para intercalar
    # Posições: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
    C.insert(i+i+1, B[i])  # lista.insert(posição, elemento)
'''

# Método 3 (alternativo moderno): Usando zip e list comprehension
# Descomente para testar este método mais pythonico
'''
C = [item for pair in zip(A, B) for item in pair]
'''

# Observações sobre os métodos:
# - Método 1: O(n) - Mais eficiente e didático
# - Método 2: O(n²) - Menos eficiente devido ao insert() que desloca elementos
# - Método 3: O(n) - Mais pythonico usando zip() e list comprehension
# - Todos os métodos assumem que A e B têm o mesmo tamanho