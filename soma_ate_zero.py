# 1. Faça um programa que peça números ao usuário até que ele digite 0. Ao final, mostre a soma de todos os números digitados.

soma = 0
numero = -1

while numero != 0:
    numero = int(input("Digite um número inteiro: "))
    soma += numero
    print(f"A soma dos números é: {soma}")
    if soma == 0:
        print("A soma atingiu zero. Encerrando o programa.")
        break