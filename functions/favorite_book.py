#escrever função que aceite um parametro title e exibir uma mensagem, chamar a função.

#função criada para aceitar um parametro
def favorite_book(title):
    """Escrever qual é o livro favorito"""
    print("Meu livro favorito é: " + title.title())

#chamada da função com o argumento
favorite_book('Alice no País das Maravilhas')