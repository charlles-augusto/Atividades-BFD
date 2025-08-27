# Crie uma função que receba uma lista de números e retorne a média deles.
def calcular_media(lista_de_numeros):
  """
  Esta função recebe uma lista de números e retorna a média deles.
  Retorna 0 se a lista estiver vazia para evitar erro de divisão por zero.
  """
  if not lista_de_numeros:
    return 0
  
  soma_total = sum(lista_de_numeros)
  quantidade = len(lista_de_numeros)
  return soma_total / quantidade

# Exemplo de uso:
numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print(f"A média da lista é: {media}")  # Saída: A média da lista é: 30.0