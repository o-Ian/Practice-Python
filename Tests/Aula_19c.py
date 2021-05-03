estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = input('Digite o nome do estado: ')
    estado['sigla'] = input('Digite a sigla desse estado: ')
    brasil.append(estado.copy())
for e in brasil:
    for i in e.values():
        print(i)
