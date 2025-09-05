altura = []
idade = []

for i in range(2):
    idade_pessoa = int(input(f"Digite a idade da pessoa {i+1}: "))
    altura_pessoa = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    idade.append(idade_pessoa)
    altura.append(altura_pessoa)

max_height_index = altura.index(max(altura))
max_idade_index = idade.index(max(idade))

print(f"A idade da pessoa mais velha é: {idade[max_idade_index]} anos")
print(f"A altura da pessoa mais alta é: {altura[max_height_index]} metros")
