n = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
nextenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
      'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
nd = 2
error = ''

while True:
    nd = int(input(f'{error}Digite um número entre 0 e 20: '))
    if nd not in n:
        error = 'Tente novamente. '
    else:
        error = ''
        break

print(f'Você digitou o número {nextenso[nd]}.')
