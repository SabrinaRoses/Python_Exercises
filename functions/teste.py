#criar uma lista que mostre os nomes dentro de uma função
lista_nomes = ['Karen', 'João', 'Ju', 'Raffa', 'Sabrina']

#criar função para armazenar a lista
def nomes(lista_nomes):
    """Imprimir listas de nomes"""
    for nome in lista_nomes:
        print(nome)

#chamar a função

#Fazer uma nova função que adicione a string "especial" frente a cada nome
def especial(lista_nome):
    #fazer uma comprenssão de listas e retornar o valor
    return(['Especial ' + nome for nome in lista_nomes ])
#chamar as funções
nomes(especial(lista_nomes))
