#Progama para ler o arquivo numero_favorito e verificar se a entrada ficou salva na memoria
import json

#chamando o arquivo 
filename = 'number.json'
#abrindo o arquivo no modo leitura
with open(filename) as f_obj:
    #usando a função json.load() para carregar informações armazenadas em numbers.json e as guardamos na variavel number
    number = json.load(f_obj)

    print("Eu sei qual é o seu número favorito! é o {} ".format(number))
