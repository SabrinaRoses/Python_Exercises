#criar uma lista numa função 
lista=["Sabrina", "Pedro", "Joana", "Juliane", "Polly"]
#função para chamar a lista de mágico
def show_magicians(lista):
    """imprimir lista de mágicos"""
#mostrar todos os nomes dos mágicos
    for magico in lista:
        print(magico)  
#chamar uma função que adicione "o grande" em cada mágico
def make_great(lista):
    #feita uma compreeensão de lista para concatenar a string "o grande" frente a cada item da lista
    return (['O grande ' + magico for magico in lista ])

#chamar a função da lista e inserir a função da string "O grande" dentro de make_great
#Usamos make_great como argumento.
show_magicians(make_great(lista))


