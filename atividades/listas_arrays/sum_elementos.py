# Cria uma lista vazia para armazenar os números
numbers = []

# Loop para pedir 5 números ao usuário
for i in range(5):
    # Recebe o número do usuário e converte para float
    num = float(input(f"Digite o número {i+1}: "))
    # Adiciona o número à lista
    numbers.append(num)

# Calcula a soma de todos os números na lista
total = sum(numbers)

# Imprime o resultado da soma
print(f"A soma de todos os números é: {total}")
