dados = {}
pessoa = {}
soma_idade = 0
mulheres = []
idade_acima = []
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = input('Sexo: ') .strip().upper()[0]
    if pessoa['sexo'] in 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    dados[pessoa['nome']] = pessoa.copy()
    r = input('Quer continuar? [S/N]: ') .strip().upper()[0]
    if r in 'N':
        break
media_idade = soma_idade/len(dados)
print(f'{len(dados)} pessoas foram cadastradas.')
print(f'A média de idade das pessoas cadastradas é {media_idade:.1f}.')
print(f'Todas as mulheres cadastradas: {mulheres}.')
print(f'Lista de pessoas que estão acima da média:\n ')

for k, v in dados.items():
    if v['idade'] > media_idade:
        print(f'{k} = {v}')
        print()
