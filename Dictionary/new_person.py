from turtle import title


new_person = {'first_name' : 'Juliane', 'last_name': 'Ribeiro', 'age': '30', 'city': 'BSB'}
print("Primeiro nome: " + new_person['first_name'].title(),
    "\nÚltimo Nome: " + new_person['last_name'].title(),
    "\nIdade: " + new_person['age'],
    "\nCidade: " + new_person['city'].title())