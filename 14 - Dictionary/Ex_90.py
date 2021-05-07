dados = {}
dados['Nome'] = input('Digite o nome do aluno: ')
dados['Média'] = float(input('Digite a média do aluno: '))
if dados['Média'] >= 7:
    dados['Situação'] = 'APROVADO'
elif 5 <= dados['Média'] < 7:
    dados['Situacão'] = 'RECUPERAÇÃO'
else:
    dados['Situacão'] = 'REPROVADO'
for k, v in dados.items():
    print(f'{k} é igual a {v}')
