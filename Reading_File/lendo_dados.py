#Para testar o exemplo precisamos de um arquivo salvo dentro do diretorio em um editor de texto
#Para realizar qualquer tarefa com arquivos, mesmo que seja apenas exbir o seu conteúdo. É necesssárop usar a função open()

#A palavra reservada with fecha o arquivo depois que não for mais necessário usa-lo (Poderia ser usado close, mas poderia continuar abert apos bugs)
#função open devolve um objeto que presenta o arquivo, então é necessário ter um argumento dentro dos parenteses (Nome do arquivo)
with open('teste.txt') as file_object:
    #usamos o metodo read e armazenamos o arquivo txt numa longa string(contents)
    contents = file_object.read()
    print(contents)

#única diferença é que a função read, devolve uma linha em branco apos a leitura do arquivo, caso queira remover a linha basta usar
# - o metodo rstrip
    print(contents.rstrip())

#rsplit divide a string devolve como uma lista
    print(contents.rsplit())