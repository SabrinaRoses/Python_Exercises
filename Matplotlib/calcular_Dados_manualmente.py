#Fazer um laço for Python aos inves de uma lista.

import matplotlib.pyplot as plt

x_values = list(range(1, 1001)) #Laço for que vai de 1 a 1000
y_values = [x**2 for x in x_values] # o Y_values percorre os laço de x value e eleva cada número ao quadrado.

#Passando valores para o scatter

plt.scatter(x_values, y_values, edgecolors='none',  s=40) #Edgecolor remove o contorno

#Define o titulo do gráfico
plt.title("Square Numbers", fontsize = 24)

#Define os nomes dos eixos
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square Value", fontsize = 14)

#Mostrando o gráfico 
plt.show()

#Define o tamanho de rotulos de marcação
plt.tick_params(axis="both", labelsize = 14)