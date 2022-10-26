#o exemplo a seguir armazena as linhas do arquivo de texto em uma lista, no bloco with e em seguida, exibe as linhas fora desse bloco

filename =  'teste.txt'

#abrir o arquivo
with open(filename) as file_object:
    """metodo readlines armazena cada linha do arquivo em uma lista. 
        a lista então será armazenada em lines, com qual podemos trabalhar depois que o 
        bloco with acabar"""
    lines = file_object.readlines()
    #for para leitura de linhas
    for line in lines:
        print(line.rstrip())

#depois de ler um arquivo em memoria poderemos fazer o que quisermos com os Dados