rios = {'Nilo':'Egito','Amazonas':'Brasil','yangtze':'china'}

for rio,pais in rios.items():
    print(rio.title() + " runs for " + pais.title())

#laço para exibir nome de cada rio no dicionario
for key in rios.keys():
    print(key.title())

#laço para exibir os valores de cada chave

for value in rios.values():
    print(value.title())