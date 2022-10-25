#Lendo um arquivo linha por linha.
file_text = 'capitulo_10_Resenha.txt'

with open(file_text) as file_object:
    for line in file_object:
        print(line)
