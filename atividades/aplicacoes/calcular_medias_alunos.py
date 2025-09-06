# Inicializa uma lista vazia para armazenar as notas de todos os alunos
notas = []
# Loop para coletar as notas de 2 alunos
for i in range(2):
    # Inicializa uma lista vazia para armazenar as notas de um aluno específico
    aluno_notas = []
    # Loop para coletar 3 notas para cada aluno
    for j in range(3):
        # Solicita ao usuário que digite a nota e a converte para float
        nota = float(input(f"Digite a {j+1}ª nota do {i+1}º aluno: "))
        # Adiciona a nota à lista de notas do aluno atual
        aluno_notas.append(nota)
    # Adiciona a lista de notas do aluno atual à lista geral de notas
    notas.append(aluno_notas)

# Loop para iterar sobre as notas de cada aluno e calcular a média
for i, aluno_notas in enumerate(notas):
    # Calcula a média das notas do aluno
    media = sum(aluno_notas) / len(aluno_notas)
    # Imprime a média do aluno formatada com duas casas decimais
    print(f"A média do {i+1}º aluno é {media:.2f}")