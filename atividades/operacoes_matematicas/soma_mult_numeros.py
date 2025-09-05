# Lista para armazenar os números inseridos pelo usuário
numeros = []

# Loop para coletar 50 números do usuário
for i in range(50):
    while True:
        try:
            # Solicita e converte a entrada do usuário para inteiro
            num = int(input(f"Insira um número inteiro {i+1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido")

# Calcula a soma de todos os números
sum_numbers = sum(numeros)

# Calcula a multiplicação de todos os números
mult_numeros = 1
for num in numeros:
    mult_numeros *= num

# Exibe os resultados
print("\nOs números inseridos são:")
print(numeros)
print(f"\nSoma de todos os números: {sum_numbers}")
print(f"Multiplicação de todos os números: {mult_numeros}")
