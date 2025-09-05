numbers = (1, 3, 5, 7, 9, 11, 13, 15)
user_num = int(input("Digite um número para buscar: "))

if user_num in numbers:
    print(f"O número {user_num} está na tupla!")
else:
    print(f"O número {user_num} não está na tupla.")
