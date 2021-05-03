pessoas = {'nome': 'Ian', 'idade': 17, 'sexo': 'M', }
'''print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')'''
pessoas['peso'] = 50
for k, v in pessoas.items():
    print(k, v)
