#Neste programa usaremos python para criar um possivel passeio aleatório
#E então usaremos matplotlib para criar uma representação visual dos dados gerados

import matplotlib.pyplot as plt
from random import choice #choice para decidir qual opção utilizaremos sempre que uma decisão for tomada.


#Criando classe RandomWalk
#Precisa de tres atributos: 1 variavel para o numero de pontos do passeio e 2 listas para armazenar os valores de cooordenadas x e y

class RandomWalk():
    """Tomará decisões aleatórias sobre a direção que o passeio deve seguir"""

    def __init__(self, num_points=5000):
        """Inicia os atributos de um passeio"""
        self.num_points = num_points

    #Todos os passeios começam em (0,0)
        self.x_values = [0]
        self.y_values=[0]

    #usaremos fill_walk para preencher nosso passeio com pontos e determinar a direção de cada passo

    def fill_walk(self):
        """Calcula todos os pontos do passeio"""
    
    #Continua dando passos até que o passeio alcane o tamanho desejado
    
        while len(self.x_values) < self.num_points:
            #Decide direção a ser seguida e distância a ser percorrida nessa direção
            #o metodo simula 4 decisões aleatorias (choice)
            x_direction = choice([1,-1]) #choice devolve 1 para direita e -1 para esquerda e decide o movimento
            x_distance = choice([0 , 1, 2, 3, 4]) #Seleciona a distância a ser percorrida nessa direção, selecionando um inteiro de 0 a 4
            #x_step determina o tamanho de cada passo nas direções x e y
            x_step = x_direction * x_distance #se o resultado for positivo move-se para direita, negativo para esquerda
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            #ystep determina o tamanho de cada passo nas direções x e y
            y_step = y_direction * y_distance #Resultado positivo move-se para cima, e negativo movimento para baixo

            #Rejeita os movimentos que não vão a lugar nenhum
            if x_step == 0 and y_step == 0:
                #Se o valor tanto de stepx e stepy forem 0, o passeio será interrompido, mas o laço continua
                continue 
            #Calcula os próximos valores de x e de Y
            #Somamos o valor em x_step ao ultimo valor armazenado em x_values [-1]. Faz.se o mesmo para os valores de y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

