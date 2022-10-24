#Escreva um programa que pergunte qual é o número favorito de um usuário. 
#Use Json.dump() para armazenar o número em um arquivo e mostre para o usuário que você sabe.
#json.dump() armazena o conjnto de informações
#json.load() Lê o número de volta para a memoria

import json

#recebendo número do usuario
number = int(input("Digite o seu número favorito:\n"))

#escolhendo nome do arquivo e armazenando
filename = 'number.json'

#Abrindo o arquivo em modo de escrita
with open(filename, 'w') as f_obj:
    #usando a função json.dump() para armazenar o número no arquivo 'number.json'
    json.dump(number,f_obj)
