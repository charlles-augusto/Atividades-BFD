# Script: notas_e_media.py
# Descrição: Calcula a média de notas de uma turma de 40 alunos
# Objetivo: Demonstrar coleta de dados, validação de entrada e cálculo estatístico

# Inicialização da lista para armazenar todas as notas da turma
# Cada elemento representa a nota de um aluno individual
notas = []

# Coleta de dados
# Loop para coletar as notas de 40 alunos
# range(40) gera números de 0 a 39
for i in range(40):
    # Loop de validação infinito
    # Continua pedindo até que uma nota válida seja digitada
    while True:
        try:
            # Solicita a nota do aluno (i+1) e converte para float
            # O +1 em i+1 ajusta a numeração para o usuário (1 a 40)
            grade = float(input(f"Digite a nota do aluno {i+1}: "))
            
            # Validação do intervalo da nota (0 a 10)
            # Só aceita valores dentro do intervalo escolar padrão
            if 0 <= grade <= 10:
                # Nota válida: adiciona à lista e sai do loop while
                notas.append(grade)
                break
            else:
                # Nota fora do intervalo: avisa o usuário e continua no loop
                print("A nota deve estar entre 0 e 10")
                
        except ValueError:
            # Tratamento de erro para entrada inválida (não numérica)
            # Captura quando o usuário digita algo que não é número
            print("Por favor, digite um número válido")

# Cálculo estatístico
# Calcula a média aritmética das notas da turma
# sum(notas) soma todas as notas coletadas
# len(notas) retorna o número total de notas (deve ser 40)
media = sum(notas) / len(notas)

# Exibição dos resultados
# Primeiro mostra todas as notas digitadas para referência
print("\n=== Notas digitadas ===")

# enumerate() retorna pares (índice, valor)
# O parâmetro 1 em enumerate(notas, 1) faz a contagem começar em 1
for i, nota in enumerate(notas, 1):
    print(f"Nota {i}: {nota}")

# Exibe a média final da turma
# :.2f formata o número para mostrar apenas 2 casas decimais
print(f"\n=== Resultado Final ===")
print(f"Média da turma: {media:.2f}")

# Informações adicionais:
# - Total de alunos processados: len(notas)
# - Nota mínima: min(notas)
# - Nota máxima: max(notas)
# - Estas estatísticas podem ser adicionadas facilmente se necessário