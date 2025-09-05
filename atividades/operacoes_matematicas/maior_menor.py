numbers = input("Digite inteiros separados por espaços: ").split()
numbers = [int(num) for num in numbers]

max_value = max(numbers)
min_value = min(numbers)

print(f"O maior valor é: {max_value}")
print(f"O menor valor é: {min_value}")
