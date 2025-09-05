# Lê os valores para a e b
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
# Imprime os valores originais
print(f"\nValores originais: a = {a}, b = {b}")

# Troca os valores usando uma variável temporária
temp = a
a = b
b = temp

# Imprime os valores trocados
print(f"Valores trocados: a = {a}, b = {b}")
