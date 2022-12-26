#Gráfico Linear Simples

import matplotlib.pyplot as plt

squares = [1,4,9,16,25] #Se não definirmos os valores de entrada a bibliote começa sempre com zero, podendo causar erros.
#Podemos fazer da seguinte forma, definindo sempre o valor de entrada e saída.
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 5)

plt.plot(squares, linewidth = 5) #LineWidth define a espessura da linha.

#Define o titulo do gráfico e nomeia os eixos.
plt.title("Squares Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square Value", fontsize=14)
#Define o tamanho dos rotulos de marcação 
plt.tick_params(axis='both', labelsize=14)

plt.show()