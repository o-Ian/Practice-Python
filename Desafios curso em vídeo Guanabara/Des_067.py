while True:
    n = int(input('Digite um número: '))
    if n <= 0:
        break
    print('-' *20)
    for c in range(1, 11):
        print(f'{c}*{n} = {c*n}')
    print('-' * 20)
print('Programa encerrado, foi muito bom ajudar você!')
