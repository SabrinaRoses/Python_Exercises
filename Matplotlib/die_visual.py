#Lançando o dado
#criando um histograma (COm lista de frequencia podemos criar um histograma de resultado)
#Histrograma: Gráfico de barras que mostra a frequencia de ocorrencia de determinados resultados.

import pygal


from die import Die

#Cria um D6

die = Die() #Instancia  de como default

#Faz alguns lançamentos e armazena-os em uma lista
results = [] #Create list

for roll_num in range(1000): #Lançando o dado 1000x
    result = die.roll() #Result recebe valor aleatorio entre 1 e 6
    results.append(result) #Lista results recebe cada valor aleatorio pego no result
print(results) #Printa o resultado.

#Analisa o resultado

frequencies = [] #Lista vazia para armazenar o número de vezes que cada valor foi tirado.
for value in range(1, die.num_sides+1): #Percorremos os valores possiveis com um laço de 1 a 6
    frequency = results.count(value)  #Contamos quantas vezes cada número aparece em results 
    frequencies.append(frequency) #concatenamos o valor na lista frequencies
print("\n",frequencies)#Então exibimos a lista antes de criar a visualização

#visualiza resultados
hist = pygal.Bar() #Gerando gráfico de barras

#Definindo titulos do histograma
hist.title = "Results of rolling one D6 1000 times" 

#Criando rotulos dos eixos
hist.x_labes = ['1', '2', '3', '4', '5', '6']
hist.y_title = "Frequency of Result"

#Acrescentando serie de valores ao gráfico
hist.add('D6', frequencies) #Passando um rotulo para o conjunto de valores.
hist.render_to_file('die_visual.svg') #Redenrizando um gráfico em um arquivo SVG

