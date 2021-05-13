def leiaDinheiro(msg):
    n = input(msg).strip()
    while True:
        error = f'\033[1;31mERRO! {n} é um preço inválido!\033[m'
        if not n.isdecimal() or not n.isnumeric() or n == '':
            print(error)
            n = input(msg)
        else:
            break


leiaDinheiro('Digite um número: ')
