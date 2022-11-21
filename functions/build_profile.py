#Os asteriscos duplos antes do parâmetro **user_info fazem python criar um dicionário vazio chamado user_info e colocar quaisquer
#-- continuação --- quaisquer pares nome-valor recebidos nesse dicionário

def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário"""
#profile = dicionário vazio para armazernar o perfil do usuário
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
        return profile


user_profile = build_profile('albert','einstein', location ='princeton',field='physics',teste ='samara')
print(user_profile)