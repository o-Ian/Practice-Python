def moeda(n):
    n = str(n).replace('.', ',')
    n = 'R$' + n
    return n


def aumentar(n, porcentagem, form=False):
    preco_novo = n + (n * (porcentagem/100))
    if form:
        return moeda(preco_novo)
    return preco_novo


def diminuir(n, porcentagem, form=False):
    preco_novo = n - (n * (porcentagem/100))
    if form:
        return moeda(preco_novo)
    return preco_novo


def dobro(n, form=False):
    dobro = n * 2
    if form:
        return moeda(dobro)
    return dobro


def metade(n, form=False):
    metade = n/2
    if form:
        return moeda(metade)
    return metade


def resumo(n, porc_aumento, porc_diminuir):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado:{moeda(n):>11}')
    print(f'Dobro do preço: {dobro(n, True):>11}')
    print(f'Metade do preço:{metade(n, True):>11}')
    print(f'{porc_aumento}% de aumento: {aumentar(n, porc_aumento, True):>11}')
    print(f'{porc_diminuir}% de redução: {diminuir(n, porc_diminuir, True):>11}')
