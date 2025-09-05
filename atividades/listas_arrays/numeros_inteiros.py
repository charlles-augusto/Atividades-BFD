# Cria uma lista vazia para armazenar os números
numeros = []

# Loop que solicita 5 números inteiros do usuário
for i in range(5):
    # Recebe o número do usuário e converte para inteiro
    num = int(input(f"Digite um número inteiro #{i+1}: "))
    # Adiciona o número à lista
    numeros.append(num)

# Imprime a lista completa de números
print(numeros)
