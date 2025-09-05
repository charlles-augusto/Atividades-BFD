# Lista para armazenar os números reais
numeros = []

# Loop para coletar 10 números do usuário
for i in range(10):
    num = float(input(f"Digite um número real #{i+1}: "))
    numeros.append(num)

# Imprime os números em ordem inversa
print("\nNúmeros em ordem inversa:")
for num in reversed(numeros):
    print(num)
