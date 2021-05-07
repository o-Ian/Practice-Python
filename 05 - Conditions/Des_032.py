from datetime import date
ano = int(input('Digite um ano, coloque 0 se desejar pegar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano // 1 % 10 == 0 and ano // 10 % 10 == 0:
    if ano % 400 == 0:
        print('O ano {} é bissexto!' .format(ano))
    else:
        print('O ano {} não é bissexto!' .format(ano))
else:
    if ano % 4 == 0:
        print('O ano {} é bissexto!' .format(ano))
    else:
        print('O ano {} não é bissexto!' .format(ano))
