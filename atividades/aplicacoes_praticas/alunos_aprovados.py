media_aluno = []

for aluno in range(10):
    notas = []
    print(f"\nAluno {aluno + 1}:")
    
    for nota in range(4):
        while True:
            try:
                nota = float(input(f"Insira nota {nota + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota deve estar entre 0 e 10")
            except ValueError:
                print("Por favor, insira um número válido")
    
    media = sum(notas) / len(notas)
    media_aluno.append(media)

aprovados = sum(1 for media in media_aluno if media >= 7.0)
reprovados = sum(1 for media in media_aluno if media < 7.0)


print(f"\nNúmero de alunos com média >= 7.0: {aprovados}")
print(f"\nNúmero de alunos com média < 7.0: {reprovados}")