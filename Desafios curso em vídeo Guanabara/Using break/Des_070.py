soma = mais1000 = preco_barato = 0
nome_barato = ' '

while True: 
    nome = input('Digite o nome do produto: ')
    p = 0
    while p <= 0:
        p = float(input('Qual o preço desse produto? R$'))
    soma += p
    if p > 1000:
        mais1000 += 1
    if preco_barato == 0:
        preco_barato = p
        nome_barato = nome
    else:
        if preco_barato > p:
            preco_barato = p
            nome_barato = nome

    r = ' '
    while r not in 'SN':
        r = input('Você quer continuar? [S/N] ') .strip() .upper()[0]

    if r == 'N':
        break
print('-' *30)
print(f'Você gastou o total de R${soma:.2f}.\nForam cadastrados {mais1000} produtos de mais de R$1000.\nO produto mais '
      f'barato foi {nome_barato}.')
