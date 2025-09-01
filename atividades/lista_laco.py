n = int(input("Digite um número N: "))

even_numbers = []

for i in range(1, n + 1):
    if i % 2 == 0:
        even_numbers.append(i)

print(f"Números pares de 1 até {n}: {even_numbers}")
