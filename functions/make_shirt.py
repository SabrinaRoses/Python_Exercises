#Fazer uma função que pede o número de uma camiseta e a frase desejada.

#criando funçao com parametros tamanho e frase
def make_shirt(tamanho = 'grande', texto = 'eu amo python'):
    #Mostrar o tamanho da camiseta com a frase
    print("I would like the a T-shirt: " + tamanho)
    print("The phare is: " + texto)

make_shirt('M', 'Foda-se o estado!\n')
make_shirt()