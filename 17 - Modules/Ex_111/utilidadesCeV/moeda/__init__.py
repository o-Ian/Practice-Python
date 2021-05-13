def moeda(n, moeda='R$'):
    return f'{moeda}{n:>.2f}' .replace('.', ',')


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
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True):}')
    print(f'{porc_aumento}% de aumento: \t{aumentar(n, porc_aumento, True)}')
    print(f'{porc_diminuir}% de redução: \t{diminuir(n, porc_diminuir, True)}')
