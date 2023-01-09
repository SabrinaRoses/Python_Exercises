#Plotando o random_walk.py

import matplotlib.pyplot as plt

#Importando o arquivo Class
from random_walk import RandomWalk

#Continua criando passeios aleatóriosenquanto o progama estiver ativo
while True:
    #Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()
    #Passando valores de x e y
    plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, edgecolors='none', cmap=plt.cm.hot,  s=15)

    #Definindo titulos
    plt.title("Randow Walk", fontsize= 14)

    #enfatizar o primeiro e o ultimo ponto
    plt.scatter(0, 0, c='green', edgecolors='none', s=100) #Ponto inicial
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=100) #ponto final

    #removendo os eixos
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    #mostrando
    plt.show()

    #condição encerramento/continuação
    keep_running = input("Make another Walk? (y/n): ")
    if keep_running == 'n':
        break

