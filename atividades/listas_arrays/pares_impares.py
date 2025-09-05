numeros = []
pares = []
impares = []

for i in range(20):
    num = int(input(f"Digite um número inteiro #{i+1}: "))
    numeros.append(num)
    
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("\nTodos os números:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
