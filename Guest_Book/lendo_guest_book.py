#Lendo o arquivo lista_usuario.py
#Caso queira limpar a lista, a função está como comentário

#Limpando um arquivo
#with open("guest_book.txt", 'r+') as f:
#    f.truncate(0)

with open('guest_book.txt') as file_object:
    contents = file_object.read()
    print(contents)
