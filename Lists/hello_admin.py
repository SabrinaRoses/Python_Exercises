#vericar se o usuário é o admin.
list_users = ['admin', 'sab', 'login', 'ana', 'joao']

if list_users == False:
        print("Precisamos de novos usuários")
for list_user in list_users:
    if list_user == 'admin':
        print("Welcome, admin")
    elif list_user != 'admin':
        print("welcome," + list_user + "!")
    