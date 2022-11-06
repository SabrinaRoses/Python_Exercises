#verificar como andar por arrays com np
current_users = ['admin', 'sab', 'sama', 'renan', 'ju']
new_users = ['admin', 'sab', 'pedro', 'sol', 'raffa']

for new_user in new_users:
    new_users = new_user.upper()

for current_user in current_users:
    current_users = current_user.upper()


for new_user in new_users:
    new_users = new_user.upper()
    for current_user in current_users:
        current_users = current_user.upper()
        if new_user == current_user:
            print("Este nome já está em uso,")

