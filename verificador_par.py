# 8. Crie uma função que receba um número e retorne True se ele for par e False caso contrário.
def eh_par(numero):
  """
  Esta função recebe um número e retorna True se ele for par e False caso contrário.
  """
  return numero % 2 == 0

# Exemplo de uso:
print(f"O número 10 é par? {eh_par(10)}")  # Saída: O número 10 é par? True
print(f"O número 7 é par? {eh_par(7)}")    # Saída: O número 7 é par? False