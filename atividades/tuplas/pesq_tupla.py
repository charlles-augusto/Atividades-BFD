# Tupla com números ímpares de 1 a 15
numbers = (1, 3, 5, 7, 9, 11, 13, 15)

# Solicita ao usuário um número para buscar na tupla
user_num = int(input("Digite um número para buscar: "))

# Verifica se o número está presente na tupla
if user_num in numbers:
    print(f"O número {user_num} está na tupla!")
else:
    print(f"O número {user_num} não está na tupla.")
