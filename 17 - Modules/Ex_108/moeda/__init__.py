def aumentar(n, porcentagem):
    preco_novo = n + (n * (porcentagem/100))
    return preco_novo


def diminuir(n, porcentagem):
    preco_novo = n - (n * (porcentagem/100))
    return preco_novo


def dobro(n):
    return n * 2


def metade(n):
    return n/2


def moeda(n):
    n = str(n).replace('.', ',')
    n = 'R$'+n
    return n
