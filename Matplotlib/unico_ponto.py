#Como plotar um único ponto

import matplotlib.pyplot as plt

#chame o metodo scatter e selecione os pontos que deseja exibir
plt.scatter(2, 4, s=200) #S=200 define o tamnho do ponto . 

#Define o titulo do gráfico
plt.title("Square Numbers", fontsize = 24)

#Define o titulo do eixos e tamanho da fonte
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of label", fontsize= 14)

#função que mostra o gráfico
plt.show()