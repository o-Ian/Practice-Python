def fatorial(n, show=False):
    """
    :param n: Recebe o número que será calculado
    :param show: True para mostrar o cálculo que foi feito
    :return: Retorna o valor do fatorial de n
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            if c > 1:
                print(c, end=' x ')
            else:
                print(f'{c} = ', end='')
        f *= c

    return f


print(fatorial(6, False))
