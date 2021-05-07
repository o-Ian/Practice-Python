dados = []
lista = []
n = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    lista.append(dados[:])

    dados.clear()
    resp = input('Quer continuar? [S/N]: ')
    if resp in 'Nn':
        break
print('=-' * 30)
print('No   Nome               MÉDIA')
print('-' * 30)
for n, p in enumerate(lista):
    print(f'{n:<5}{p[0]:15}{(p[1] + p[2]) / 2:>8}')

print('-' * 35)

while True:
    nota_aluno = int(input('Mostrar a nota de qual aluno? [999 interrompe]: '))
    if nota_aluno == 999:
        break
    print('-' * 35)
    print(f'As notas de \033[1m{lista[nota_aluno][0]}\033[m são {lista[nota_aluno][1::]}')
    print('-' * 35)
