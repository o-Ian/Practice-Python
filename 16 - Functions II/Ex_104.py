def leiaInt(imput):
    n = input(imput)
    while not n.isnumeric():
        print(f'\033[1;31mErro! O valor digitado não é um número.\033[m ')
        n = input(imput)
    return n


num = leiaInt('Digite um número: ')
print(f'O número digitado foi {num}.')
