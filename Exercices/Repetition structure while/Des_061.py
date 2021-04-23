a1 = int(input('Qual o primeiro termo? '))
r = int(input('Qual é a razão dessa PA? '))
c = 1
termo = a1
while c < 11:
    print('{} -> '.format(termo), end = '')
    termo += r
    c += 1
print('ACABOU')
