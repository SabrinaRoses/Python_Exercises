from queue import PriorityQueue

favorite_number = {'Sabrina' : '16', 'Juliane' : '13', 'polly' : '10'}

for name, age in favorite_number.items():
    print("\nName: " + name.title())
    print("Age: " + age + " years old.\n")

######################################################################

friends = ['Sabrina', 'Juliane']

for name in favorite_number.keys():

    if name in friends:
        print("Hi, " + name.title() +
         ", I see your age is: " + favorite_number[name].title() + "!" )
#VERIFICAR SE UM NOME NÃO ESTÁ NA LISTA
if 'joao' not in favorite_number.keys():
    print("This name is not present in the list")

