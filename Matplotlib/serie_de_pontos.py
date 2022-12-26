#Plotando uma série de pontos com scatter()

import matplotlib.pyplot as plt

#Para plotar uma série de pontos passamos uma lista separadas de valores para x e y para scatter()

#Definindo listas
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

#Passando listas para o scatter
plt.scatter(x_values, y_values, s=100)

#Mostrando gráfico
plt.show()