def leiaDinheiro(msg):
    n = input(msg).strip().lower().replace(' ', '').replace(',', '.')
    while True:
        error = f'\033[1;31mERRO! {n} é um preço inválido!\033[m'
        if n.isalpha() or n.strip() == '':
            print(error)
            n = input(msg)
        else:
            nTemNumero = 0
            for c in n:
                if c.isalpha():
                    nTemNumero += 1
            if nTemNumero >= 1:
                print(error)
                n = (input(msg))
            else:
                break

    return float(n)
