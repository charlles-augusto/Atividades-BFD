notas = []

for i in range(40):
    while True:
        try:
            grade = float(input(f"Digite a nota do aluno {i+1}: "))
            if 0 <= grade <= 10:
                notas.append(grade)
                break
            else:
                print("A nota deve estar entre 0 e 10")
        except ValueError:
            print("Por favor, digite um número válido")

media = sum(notas) / len(notas)

print("\nNotas digitadas:")
for i, nota in enumerate(notas, 1):
    print(f"Nota {i}: {nota}")

print(f"\nMédia da turma: {media:.2f}")