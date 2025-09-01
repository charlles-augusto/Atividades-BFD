# Get input from user
n = int(input("Digite um número N: "))

# Create empty list to store even numbers
even_numbers = []

# Loop from 1 to N and add even numbers to list
for i in range(1, n + 1):
    if i % 2 == 0:
        even_numbers.append(i)

# Print the list of even numbers
print(f"Números pares de 1 até {n}: {even_numbers}")
