# Lista para armazenar os números inseridos pelo usuário
numeros = []

# Loop para coletar 10 números do usuário
for i in range(10):
    num = int(input(f"Insira um número inteiro {i+1}: "))
    numeros.append(num)

# Calcula a soma dos quadrados dos números usando list comprehension
soma_quadrados = sum(x**2 for x in numeros)

# Exibe o resultado da soma dos quadrados
print(f"\nA soma dos quadrados é: {soma_quadrados}")
