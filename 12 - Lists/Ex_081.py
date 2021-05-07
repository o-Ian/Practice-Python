lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = input('Você quer continuar? [S/N]: ') .upper().strip()[0]
    if r in 'N':
        break
print(f'Foram digitados {len(lista)} números.')
if 5 in lista:
    print(f'O número cinco foi digitado e está na posição {lista.index(5)}.')
else:
    print(f'O número cinco não foi digitado!')
lista.sort(reverse=True)
print(f'Os números digitados de forma decrescente: {lista}.')
