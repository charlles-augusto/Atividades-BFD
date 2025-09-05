# Script: alunos_aprovados.py
# Descrição: Sistema de gerenciamento de notas escolares
# Objetivo: Calcular médias de alunos e determinar aprovações/reprovações

# Lista para armazenar as médias finais de todos os alunos
# Cada elemento representa a média de um aluno
media_aluno = []

# Processamento de dados dos alunos
# Loop principal para coletar notas de 10 alunos
for aluno in range(10):  # range(10) gera números de 0 a 9
    # Lista temporária para armazenar as 4 notas de cada aluno
    # É reinicializada para cada novo aluno
    notas = []
    
    # Cabeçalho identificando qual aluno está sendo avaliado
    print(f"\nAluno {aluno + 1}:")
    
    # Coleta das 4 notas de cada aluno
    # Loop interno para garantir que cada aluno tenha exatamente 4 notas
    for nota in range(4):  # range(4) gera números de 0 a 3
        # Loop infinito para validação de entrada
        # Só sai do loop quando uma nota válida é digitada
        while True:
            try:
                # Solicita a nota e converte para float (número decimal)
                # O +1 em nota+1 ajusta a numeração para o usuário (1 a 4)
                nota = float(input(f"Insira nota {nota + 1}: "))
                
                # Validação do intervalo da nota (0 a 10)
                if 0 <= nota <= 10:
                    # Nota válida: adiciona à lista e sai do loop while
                    notas.append(nota)
                    break
                else:
                    # Nota fora do intervalo: avisa o usuário e continua no loop
                    print("Nota deve estar entre 0 e 10")
                    
            except ValueError:
                # Tratamento de erro para entrada inválida (não numérica)
                print("Por favor, insira um número válido")
    
    # Cálculo da média do aluno atual
    # sum(notas) soma todas as notas do aluno
    # len(notas) retorna 4 (número de notas)
    media = sum(notas) / len(notas)
    
    # Armazena a média calculada na lista de médias
    media_aluno.append(media)

# Análise dos resultados
# Contagem de alunos aprovados (média >= 7.0)
# Expressão geradora: 1 for media in media_aluno if media >= 7.0
# sum() soma todos os 1s gerados, resultando na contagem
aprovados = sum(1 for media in media_aluno if media >= 7.0)

# Contagem de alunos reprovados (média < 7.0)
# Mesma lógica, mas com condição inversa
reprovados = sum(1 for media in media_aluno if media < 7.0)

# Exibição dos resultados finais
print(f"\n=== Resultados Finais ===")
print(f"Número de alunos com média >= 7.0: {aprovados}")
print(f"Número de alunos com média < 7.0: {reprovados}")

# Observação: O sistema considera 7.0 como nota mínima para aprovação
# Alunos com média exatamente 7.0 são considerados aprovados