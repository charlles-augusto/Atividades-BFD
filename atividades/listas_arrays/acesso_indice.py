# Script: acesso_indice.py
# Descrição: Demonstra como acessar elementos de uma lista pelo índice
# Objetivo: Ensinar indexação positiva e negativa em listas Python

# Criação de uma lista de strings com nomes de cores
# Índices: 0="azul", 1="verde", 2="vermelho", 3="amarelo"
cores = ["azul", "verde", "vermelho", "amarelo"]

# Acesso por índice positivo
# Índice 1 retorna o segundo elemento (contagem começa em 0)
# Resultado: "verde"
print("Elemento no índice 1:", cores[1])

# Acesso por índice negativo
# Índice -1 retorna o último elemento da lista
# Resultado: "amarelo"
print("Último elemento (índice -1):", cores[-1])

# Observações sobre indexação:
# - Índices positivos: 0, 1, 2, 3 (da esquerda para direita)
# - Índices negativos: -1, -2, -3, -4 (da direita para esquerda)
# - Tentar acessar índice fora do intervalo causa erro IndexError