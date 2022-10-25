#Escreva um laço while que pergunte o nome aos usuários. Quando fornecerem seus nomes, apresente uma saudação
#Acrescente uma linha que registre a visita do usuário em um arquivo chamado guest.book.txt 
#Cada entrada deve estar em uma nova linha de arquivo

continuar = True
file = 'guest_book.txt'


while continuar:
    #Pedindo nome ao usuário
    usuario = input ("Qual é o seu nome? \n")

    #Abrindo o arquivo como concatenação
    with open (file, 'a') as file_object:
        #Escrevendo todo usuário que entra no laço while
        file_object.write(usuario)
        file_object.write('\n')

    #Laço para perguntar nome
    continuar = str.lower(input("Deseja adicionar mais usuários?\n"))
    if continuar == 'yes':
        continuar = 'True'

    if continuar == 'no':
        continuar = False
    
    

    
    
    

