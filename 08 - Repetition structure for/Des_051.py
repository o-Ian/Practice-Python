a1 = int(input('Qual o primeiro termo? '))
r = int(input('Qual é a razão dessa PA? '))
for c in range(1, 11):
    print(a1 + (c - 1) * r, end=' -> ')
print('ACABOU')
