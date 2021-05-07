from datetime import date
ano = int(input('Digite o ano em que você nasceu! '))
if (date.today().year - ano) > 18:
    print('Já passou {} anos do seu alistamento!' .format(date.today().year - ano - 18))
elif (date.today().year - ano) < 18:
    print('Faltam {} anos para você se alistar!' .format(18 - (date.today().year - ano)))
else:
    print('Está na hora de você se alistar, seu escravo!')
