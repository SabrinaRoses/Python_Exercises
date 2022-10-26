#path de arquivos diz a Python para procurar o arquivo em um local especifico do sistema

#Essa linha diz para Python procurar o arquivo .txt desejado na pasta text_files e supõe que está essa pasta está localizada em python_work
#(E ESTÁ)
  #  with open('text_file/ nome_do_arquivo.txt') as file

#Podemos dizer a Python exatamente em que local o arquivo está no seu computador, não importa o lugar em que o programa em execução
# - NO momento esteja armazenado. - Isso é chamada de path absoluto do arquivo. *Use o absoluto se o relativo não funcionar
#Paths absolutos geralmente sáo mais longos que paths relativos, portanto é conveniente armazena-los em uma variavel e então passar ess variavel para open

#usar dupla barrras invertida elimina erros do windows
file_path = ("C:\\Users\\Sabrina Roses\\Desktop\\arduino.txt")
with open(file_path) as file_object:
    print(file_object.read())
    
    