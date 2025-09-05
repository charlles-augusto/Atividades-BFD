# Script: dias_sem.py
# Descrição: Demonstra o uso de tuplas (tuples) em Python
# Objetivo: Mostrar acesso a elementos de uma tupla e diferenciar de listas

# Criação de uma tupla com os dias da semana
# Tuplas são coleções ordenadas e imutáveis (não podem ser modificadas)
# Índices: 0="domingo", 1="segunda", 2="terça", 3="quarta", 4="quinta", 5="sexta", 6="sábado"
dias = ("domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado")

# Acesso por índice
# Índice 2 retorna o terceiro elemento (contagem começa em 0)
# Resultado: "terça"
print("Dia no índice 2:", dias[2])

# Informações sobre tuplas:
# - São definidas com parênteses () ao invés de colchetes []
# - São imutáveis: não podem ser modificadas após criação
# - São mais eficientes em memória que listas
# - Podem conter elementos de diferentes tipos
# - Mantêm a ordem dos elementos

# Exemplo de erro que ocorreria se tentássemos modificar:
# dias[2] = "terça-feira"  # Isso causaria TypeError: 'tuple' object does not support item assignment