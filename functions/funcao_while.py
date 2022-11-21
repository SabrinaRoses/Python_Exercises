#Função com dois parametros
def get_formatted_name(first_name, last_name):
    """Devolver um nome completo formatado de forma elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title() 
    #Toda vez que retornar o valor eu preciso armazena-lo em uma nova variavel


 #Pytho interpreta strings não vazias como True / Ou seja, este programa dará um loop
while True:
    
    #entrada de dados
    print("\nPlease tell me your name: ")
    print("(Enter 'q' at any time to quit )")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    #Pegando os parametros e amarzenando na variavel de formatação
    #get aceita os parametros
    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello," + formatted_name + "!")


