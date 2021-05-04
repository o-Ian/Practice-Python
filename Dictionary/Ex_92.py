from datetime import date
dados = {}
while True:
    dados['Nome'] = input('Digite seu nome: ')
    anonasc = int(input('Digite o seu ano de nascimento: '))
    dados['idade'] = date.today().year - anonasc
    dados['CTPS'] = int(input('Digite o número da sua carteira de trabalho [0 se não tiver]: '))
    if dados['CTPS'] == 0:
        break
    else:
        dados['contratacao'] = 0
        error = ''
        while dados['contratacao'] < anonasc+14:
            dados['contratacao'] = int(input(f'{error}Digite o ano de sua contratação: '))
            error = 'Você não pode trabalhar com menos de 14 anos, tente novamente...\n'
        dados['aposentadoria'] = dados['contratacao'] + 35 - anonasc
        dados['salário'] = float(input('Digite o seu salário mensal: R$'))
        break
for k, v in dados.items():
    print(f'{k} tem o valor {v}.')
