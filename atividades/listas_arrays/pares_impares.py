# Lista para armazenar todos os números digitados
numeros = []
# Lista para armazenar apenas os números pares
pares = []
# Lista para armazenar apenas os números ímpares
impares = []

# Loop para coletar 20 números do usuário
for i in range(20):
    num = int(input(f"Digite um número inteiro #{i+1}: "))
    numeros.append(num)
    
    # Verifica se o número é par ou ímpar
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Exibe os resultados
print("\nTodos os números:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
