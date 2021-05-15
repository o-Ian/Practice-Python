def leiaInt(imput):
    while True:
        try:
            n = int(input(imput))
        except:
            print(f'\033[1;31mErro! O valor digitado não é um número inteiro.\033[m')
            valido = False
        else:
            return n
            break


def leiaFloat(imput):
    while True:
        try:
            n = float(input(imput))
        except:
            print(f'\033[1;31mErro! O valor digitado não é um número inteiro.\033[m')
        else:
            return n
            break
