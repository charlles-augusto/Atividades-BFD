numbers = []

for i in range(5):
    num = float(input(f"Digite o número {i+1}: "))
    numbers.append(num)

total = sum(numbers)

print(f"A soma de todos os números é: {total}")
