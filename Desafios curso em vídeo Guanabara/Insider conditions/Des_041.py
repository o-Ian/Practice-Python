from datetime import date
n = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - n
if idade <= 9:
    cate = 'mirim'
elif idade <= 14:
    cate = 'infantil'
elif idade <= 19:
    cate = 'junior'
elif idade <= 20:
    cate = 'sênior'
else:
    cate = 'master'
print('A categoria é {}.' .format(cate.upper()))
