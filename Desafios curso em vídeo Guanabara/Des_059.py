from time import sleep
n = 0
while n != 5:
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite outro número inteiro: '))
    print('=-' * 25)
    print('Digite [1] para somar \nDigite [2] para multiplicar\nDigite [3] para saber qual número é o maior\n'
          'Digite [4] para digitar novos números\nDigite [5] para sair do programa')
    print('=-' * 25)
    n = int(input('Digite o número da operação que você deseja > '))
    if n == 1:
        print('A soma entre {} e {} é {}.' .format(n1, n2, n1+n2))
    elif n == 2:
        print('A multiplicação entre {} e {} é {}.' .format(n1, n2, n1*n2))
    elif n == 3:
        print('O maior número é o {}.' .format(n1 if n1 > n2 else n2))
    elif n == 4:
        ''
    else:
        print('-' * 23)
        print('\033[1;41mDigite um número válido!\033[m')
        print('-' * 23)
    sleep(1)
print('FIM')
