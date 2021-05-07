a1 = int(input('Qual o primeiro termo? '))
r = int(input('Qual é a razão dessa PA? '))
c = 1
termo = a1
print('=-'*25)
while c < 11:
    print('{} -> '.format(termo), end = '')
    termo += r
    c += 1
print('ACABOU')
print('=-'*25)
ax = 1
while ax != 0:
    ax = int(input('Quantos termos a mais você quer que apareça? '))
    print('=-'*25)
    for c in range(0, ax):
        print('{} -> '.format(termo), end='')
        termo += r
    print('ACABOU!')
    print('=-' * 25)
