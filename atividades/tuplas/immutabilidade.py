# Script: immutabilidade.py
# Descrição: Demonstração detalhada da imutabilidade de tuplas em Python
# Objetivo: Mostrar como trabalhar com tuplas e criar novas tuplas quando necessário

# Seção 1: Criação e exibição da tupla original
# Tuplas são criadas com parênteses e são IMUTÁVEIS após criação
minha_tupla = (1, 2, 3, 4, 5)
print("Tupla original:", minha_tupla)
print(f"Tipo: {type(minha_tupla)}")
print(f"Quantidade de elementos: {len(minha_tupla)}")

# Seção 2: Tentativa de modificação (gerará erro)
# Esta seção demonstra por que tuplas são chamadas de "imutáveis"
try:
    # Tentativa de modificar o primeiro elemento
    # Isso é impossível em tuplas, resultará em TypeError
    minha_tupla[0] = 10
except TypeError as e:
    print("\nErro ao tentar modificar a tupla:", e)
    print("Isso acontece porque tuplas são imutáveis - seus elementos não podem ser alterados após a criação")
    print("A imutabilidade garante segurança e integridade dos dados")

# Seção 3: Trabalhando com imutabilidade
# Como "modificar" uma tupla: criando uma nova tupla
# A estratégia é criar uma nova tupla com os valores desejados

# Criando nova tupla com slicing e concatenação
# minha_tupla[1:] retorna uma nova tupla com elementos do índice 1 em diante
# (10,) cria uma tupla com um único elemento (note a vírgula)
nova_tupla = (10,) + minha_tupla[1:]

# Explicação do processo:
print("\nProcesso de criação de nova tupla:")
print(f"1. Elemento novo: (10,) = {(10,)}")
print(f"2. Elementos antigos (exceto primeiro): {minha_tupla[1:]}")
print(f"3. Concatenação: (10,) + {minha_tupla[1:]} = {nova_tupla}")

# Resultados finais
print("\nResultados:")
print("Nova tupla criada:", nova_tupla)
print("Tupla original permanece inalterada:", minha_tupla)

# Observações importantes:
print("\nObservações:")
print("- Tuplas são imutáveis, mas podem ser concatenadas para criar novas tuplas")
print("- A tupla original nunca é modificada")
print("- Esta abordagem é segura para dados que não devem ser alterados")
print("- Tuplas são mais eficientes em memória que listas para dados fixos")
