n = 0
qntd = 0
cond = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        ''
    else:
        qntd += 1
        cond += n
print('Foram digitados {} números, a soma entre eles é igual a {}.' .format(qntd, cond))
