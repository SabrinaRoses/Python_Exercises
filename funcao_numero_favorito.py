#Una os dois exercicios em um único arquivo, escrita e leitura
#Caso não ache o arquivo, peça para o usuário digitar o seu número favorito novamente

import json

def obtendo_dados ():
    """Obtendo o número favorito caso esteja na memoria"""
    filename = 'number.json'
    #tente abrir o arquivo
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError: #Se não encontrar retorne nada
        return None
    else: #Senão retorne o arquivo
        return number

#mostrando ao usuário que sabemos seu número favorito
def mostrando_numero ():
    """Mostra o usuario seu número favorito"""
    #chama a função obtendo_dados e devolve o valor caso haja um
    number = obtendo_dados()
    if number: #caso exista um número faça:
        print("O seu número favorito é: {}".format(number))
    else: #caso não exista
        #peça o usuário o seu número favorito
        number = int(input("Digite o seu número favorito: "))
        #armazene os dados num arquivo json
        filename = 'number.json'
        #abra o arquivo em modo de escrita
        with open(filename, 'w') as f_obj:
            json.dump(number, f_obj) #usando json.dump para armazenar os no arquivo number
#chamando a função
mostrando_numero()

