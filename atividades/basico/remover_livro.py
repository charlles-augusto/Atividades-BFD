livros = ["O Senhor dos Anéis", "O Hobbit", "O Silmarillion"]
# Verifica se o livro "Silêncio dos inocentes" está na lista
if "Silêncio dos inocentes" in livros:
    # Se estiver, remove o livro da lista
    livros.remove("Silêncio dos inocentes")
else:
    # Se não estiver, imprime uma mensagem informando que o livro não foi encontrado
    print("Livro não encontrado")
# Imprime a lista de livros atualizada
print(livros)