def titulo(txt):
    print('~' * (len(txt)+4))
    print(f'  {txt}  ')
    print('~' * (len(txt)+4))


def ajuda(comando):
    from time import sleep
    c = 0
    while True:
        print('\033[45;30;7m', end='')
        titulo('SISTEMA DE AJUDA PyHELP')
        print('\033[m', end='')
        sleep(1)
        if c != 0:
            comando = input('-> Digite a função ou a biblioteca: ').strip().lower()
            if comando == 'fim':
                print('\033[41m', end='')
                titulo('ATÉ LOGO!')
                print('\033[m', end='')
                break

        print('\033[33;47;1m', end='')
        titulo(f'ACESSANDO O MANUAL DA BIBLIOTECA {comando}:')
        print('\033[m', end='')
        sleep(1)
        print('\033[1;33m', end='')
        help(comando)
        print('\033[m', end='')
        sleep(1)
        print('-' * 40)
        c += 1


ajuda(input)
