lista = []

for cont in range(0, 3):
    lista.append(int(input('Digite um valor: ')))

for i, c in enumerate(lista):
    print(f'Na posição {i} encontrei o valor {c}')
