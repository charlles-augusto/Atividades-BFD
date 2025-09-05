# Script: Conversão de Lista para Tupla
# Descrição: Demonstra a conversão de uma lista em tupla usando a função tuple()
# Conceito: Conversão entre estruturas de dados mutáveis e imutáveis
# Autor: Desenvolvedor Python
# Data: 2024

# Criação da lista original - Estrutura mutável
# Lista contém nomes de pessoas como strings
nomes_l = ['ana', 'joão', 'maria', 'pedro', 'juliana']

# Conversão de lista para tupla - Torna a estrutura imutável
# A função tuple() recebe uma sequência (lista, string, range, etc.) e retorna uma tupla
# A tupla resultante terá os mesmos elementos na mesma ordem, mas não poderá ser modificada
nomes_t = tuple(nomes_l)

# Saída de dados - Exibe a tupla resultante duas vezes
# Primeira exibição mostra a tupla convertida
print(nomes_t)
# Segunda exibição confirma que a tupla é idêntica na segunda impressão
print(nomes_t)

# Informações adicionais sobre a conversão
print(f"\nInformações sobre as estruturas:")
print(f"Lista original: {nomes_l}")
print(f"Tipo da lista: {type(nomes_l)}")
print(f"Tipo da tupla: {type(nomes_t)}")
print(f"Tamanho: {len(nomes_t)} elementos")
print(f"Elementos: {list(enumerate(nomes_t))}")

# Verificação de imutabilidade (comentada para não causar erro)
'''
try:
    nomes_t[0] = 'carlos'  # Esta linha causará TypeError
    print("Modificação bem-sucedida")
except TypeError as e:
    print(f"Erro ao tentar modificar: {e}")
'''

# Outras formas de criar tuplas a partir de sequências:
# 1. tuple() com string: tuple("python") → ('p', 'y', 't', 'h', 'o', 'n')
# 2. tuple() com range: tuple(range(5)) → (0, 1, 2, 3, 4)
# 3. Conversão direta: tuple([1, 2, 3]) → (1, 2, 3)

# Casos de uso para conversão lista→tupla:
# - Quando precisar garantir que os dados não serão modificados
# - Como chaves de dicionário (listas não podem ser usadas)
# - Para hashing quando elementos são imutáveis
# - Para passar dados de forma segura entre funções
