#escreva uma função que aceite uma lista de itens que uma pessoa quer em um sanduiche. A função de ve ter parametro que agrupe tantos itensquandtos 
#forem necessários

#função com 
def sand(carne, pao,**ingredientes):
    ingrediente = {}
    ingrediente['carne'] = carne
    ingrediente['pao'] = pao

    for key, value in ingredientes.items():
        ingrediente[key] = value

ingredientes = sand('mostarda', 'maionese', base = 'alface')

print(ingredientes)
