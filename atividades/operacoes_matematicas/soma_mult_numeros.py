numeros = []

for i in range(50):
    while True:
        try:
            num = int(input(f"Insira um número inteiro {i+1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido")

sum_numbers = sum(numeros)

mult_numeros = 1
for num in numeros:
    mult_numeros *= num

print("\nOs números inseridos são:")
print(numeros)
print(f"\nSoma de todos os números: {sum_numbers}")
print(f"Multiplicação de todos os números: {mult_numeros}")
