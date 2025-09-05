# Script: frutas.py
# Descrição: Demonstra como modificar elementos de uma lista existente
# Objetivo: Mostrar que listas são mutáveis (podem ser alteradas)

# Criação de uma lista inicial de frutas
# Lista original: ["maça", "laranja", "banana"]
# Índices: 0="maça", 1="laranja", 2="banana"
frutas = ["maça", "laranja", "banana"]

# Modificação de um elemento específico
# Substitui o elemento no índice 1 ("laranja") por "abacaxi"
# Isso demonstra que listas em Python são mutáveis
frutas[1] = "abacaxi"

# Exibição da lista após modificação
# Resultado esperado: ["maça", "abacaxi", "banana"]
print("Lista após modificação:", frutas)

# Observações importantes:
# - Listas usam colchetes [] e são mutáveis
# - Podemos modificar elementos individuais usando índice
# - A estrutura da lista permanece, apenas o conteúdo muda
# - Isso é diferente de tuplas, que são imutáveis
