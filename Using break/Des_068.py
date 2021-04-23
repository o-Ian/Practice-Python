from random import randint
perder = ganhou = 0

print('\n=-=-=-=-TENTE GANHAR DE MIM NO PAR OU ÍMPAR!=-=-=-=-\n')

while True:
    print('-=' * 15)
    eu = int(input('Digite um número: '))
    pc = randint(1, 100)
    par_ganhou = impar_ganhou = 0
    i_p = ' '
    while i_p not in 'IP':
        i_p = input('Você escolhe ímpar ou par? [I/P]: ') .strip() .upper()[0]
    soma = eu + pc

    print('-=' * 15)
    if i_p == 'P' and soma % 2 == 0:
        print(f'VOCÊ GANHOU!\nO computador escolheu {pc} e você {eu}, a soma disso é {soma}, que é PAR.')
        ganhou += 1
    elif i_p == 'I' and soma % 2 != 0:
        print(f'VOCÊ GANHOU!\nO computador escolheu {pc} e você {eu}, a soma disso é {soma}, que é ÍMPAR.')
        ganhou += 1
    else:
        x = ''
        if soma % 2 == 0:
            x = 'PAR'
        else:
            x = 'ÍMPAR'
        print(f'O COMPUTADOR GANHOU!\nO computador escolheu {pc} e você {eu}, a soma disso é {soma}, que é {x}.')
        perder += 1
    if perder != 0:
        break
print('-'*50)
print(f'Você PERDEU! Você conseguiu ganhar {ganhou} vezes consecutivamente!')
print('-'*50)
