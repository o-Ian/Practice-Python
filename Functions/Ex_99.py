from time import sleep


def maior(*num):
    print('Analisando os valores passados...')
    if len(num) == 0:
        num = 0
        tamanho = maior = 0
    else:
        for c in num:
            print(c, end=' ')
            sleep(0.3)
            tamanho = len(num)
            maior = max(num)

    print(f'Foram informados {tamanho} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('=-'*30)

    
maior(1, 9, 4, 6)
maior(3, 10, 15, 65)
maior()
maior(3)
