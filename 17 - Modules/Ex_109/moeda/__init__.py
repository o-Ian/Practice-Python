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
