numeros = []

for i in range(10):
    num = int(input(f"Insira um número inteiro {i+1}: "))
    numeros.append(num)

soma_quadrados = sum(x**2 for x in numeros)

print(f"\nA soma dos quadrados é: {soma_quadrados}")
