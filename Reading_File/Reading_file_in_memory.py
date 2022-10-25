#armazendo numa lista e trabalhando fora do with (lendo arquivo em memoria)
#criamos uma variavel 
filename = 'capitulo_10_Resenha.txt'
#abrindo o arquivo
with open(filename) as file_object:
    #cria uma variavel para usar no laço for, o metodo readlines() armazena cada linha de arquivo numa lista, a lista é então armazenda em lines
    #a qual podemos continunar trabalhando depois que o bloco with terminar
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
