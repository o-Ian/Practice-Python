try:
    n = int(input('Numerador: '))
    n2 = int(input('Denominador: '))
    r = n / n2
except (ValueError, TypeError):
    print(f'Tivemos um problema com o tipo de dado que você digitou!')
except ZeroDivisionError:
    print(f'Você não pode dividir por zero!')
except KeyboardInterrupt:
    print(f'O usuário preferiu não informar os dados!')
else:
    print(f'{r:.2f}')
finally:
    print(f'Volte sempre e muito obrigado!')
