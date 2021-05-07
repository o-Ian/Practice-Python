dados = []
pessoa = {}
soma_idade = 0
mulheres = []
idade_acima = []
while True:
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: ') .strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO, responda apenas com M ou F.')

    if pessoa['sexo'] in 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    dados.append(pessoa.copy())
    pessoa.clear()
    while True:
        r = input('Quer continuar? [S/N]: ') .strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO, responda apenas com S ou N!')
    if r in 'N':
        break
print(dados)
media_idade = soma_idade/len(dados)
print(f'{len(dados)} pessoas foram cadastradas.')
print(f'A média de idade das pessoas cadastradas é {media_idade:.1f} anos.')
print(f'Todas as mulheres cadastradas: {mulheres}.')
print(f'Lista de pessoas que estão acima da média de idade:\n ')
for p in dados:
    if p['idade'] > media_idade:
        print(p)
        print()
