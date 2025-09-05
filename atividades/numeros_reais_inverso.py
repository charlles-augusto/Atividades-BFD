numeros = []

for i in range(10):
    num = float(input(f"Digite um número real #{i+1}: "))
    numeros.append(num)

print("\nNúmeros em ordem inversa:")
for num in reversed(numeros):
    print(num)
