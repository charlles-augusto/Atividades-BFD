# Script: tupla_simples.py
# Descrição: Demonstração da diferença entre listas e tuplas em Python
# Objetivo: Mostrar mutabilidade vs imutabilidade e operações básicas

# Seção 1: Trabalhando com lista (mutável)
# Criação de uma lista de cores
# Listas são coleções ordenadas e MUTÁVEIS em Python
cores = ["vermelho", "verde", "azul", "amarelo", "roxo"]

# Verificação de existência de elemento na lista
# O operador 'in' verifica se um valor existe na coleção
if "azul" in cores:
    print("A cor azul está presente na lista")
else:
    print("A cor azul não está presente na lista")

# Acesso por índice - listas são indexadas a partir do 0
# Índices positivos: 0, 1, 2, 3, 4...
print(f"Primeira cor: {cores[0]}")  # Índice 0 = primeiro elemento
print(f"Segunda cor: {cores[1]}")   # Índice 1 = segundo elemento
print(f"Terceira cor: {cores[2]}")  # Índice 2 = terceiro elemento
print(f"Quarta cor: {cores[3]}")   # Índice 3 = quarto elemento
print(f"Quinta cor: {cores[4]}")    # Índice 4 = quinto elemento

# Acesso por índice negativo - conta do final para o início
# Índices negativos: -1 (último), -2 (penúltimo), etc.
print(f"Última cor usando índice negativo: {cores[-1]}")

# Seção 2: Conversão de lista para tupla
# tuple() converte uma lista em uma tupla (estrutura IMUTÁVEL)
# A tupla resultante terá os mesmos elementos, mas não poderá ser modificada
cores = tuple(cores)
print(f"\nTipo após conversão: {type(cores)}")
print(f"Conteúdo da tupla: {cores}")

# Seção 3: Demonstração de imutabilidade
# Tentativa de modificar um elemento da tupla
# Isso resultará em erro TypeError porque tuplas são imutáveis
try:
    cores[0] = "preto"
except TypeError as e:
    print("\nErro ao tentar modificar a tupla:")
    print(e)
    print("Isso demonstra que tuplas não permitem modificação de elementos")

# Observações finais:
# - Listas: usam [], são mutáveis, ideais para dados que mudam
# - Tuplas: usam (), são imutáveis, mais seguras e eficientes
# - Ambas são indexadas e aceitam elementos duplicados
