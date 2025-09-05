# Script: altura_idade_maior.py
# Descrição: Programa para coletar e analisar dados de altura e idade de pessoas
# Objetivo: Encontrar a pessoa mais velha e mais alta entre os dados coletados

# Inicialização das listas para armazenar os dados
# altura: lista para armazenar as alturas em metros (float)
# idade: lista para armazenar as idades em anos (int)
altura = []
idade = []

# Coleta de dados
# Loop para coletar informações de 2 pessoas
# range(2) gera os números 0 e 1, então i vai de 0 a 1
for i in range(2):
    # Solicita a idade da pessoa (i+1) e converte para inteiro
    # i+1 é usado para mostrar ao usuário o número correto da pessoa (1 e 2)
    idade_pessoa = int(input(f"Digite a idade da pessoa {i+1}: "))
    
    # Solicita a altura da pessoa (i+1) e converte para float (decimal)
    # Altura é solicitada em metros (ex: 1.75)
    altura_pessoa = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    
    # Adiciona os valores coletados às listas correspondentes
    # append() adiciona o elemento ao final da lista
    idade.append(idade_pessoa)
    altura.append(altura_pessoa)

# Análise dos dados coletados
# Encontra o índice da pessoa com maior altura
# max(altura) retorna o maior valor de altura
# altura.index() retorna a posição (índice) desse valor na lista
max_height_index = altura.index(max(altura))

# Encontra o índice da pessoa com maior idade
# Mesma lógica aplicada para encontrar a pessoa mais velha
max_idade_index = idade.index(max(idade))

# Exibição dos resultados
# Utiliza os índices encontrados para acessar os valores nas listas
print(f"A idade da pessoa mais velha é: {idade[max_idade_index]} anos")
print(f"A altura da pessoa mais alta é: {altura[max_height_index]} metros")

# Observação: É possível que a pessoa mais velha seja também a mais alta
# Os índices podem ser diferentes se as pessoas tiverem características diferentes
