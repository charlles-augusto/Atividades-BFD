notas = []
for i in range(2):
    aluno_notas = []
    for j in range(3):
        nota = float(input(f"Digite a {j+1}ª nota do {i+1}º aluno: "))
        aluno_notas.append(nota)
    notas.append(aluno_notas)

for i, aluno_notas in enumerate(notas):
    media = sum(aluno_notas) / len(aluno_notas)
    print(f"A média do {i+1}º aluno é {media:.2f}")