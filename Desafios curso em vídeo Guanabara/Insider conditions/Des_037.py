n = int(input('Digite um número: '))
num = int(input('Digite 1 para converter para binário.\n'
            'Digite 2 para converter para octal.\n'
            'Digite 3 para converter para hexadecimal.\n'
            'Sua opção: '))
if num == 1:
    print('O número {} convertido para binário é: \n{}' .format(n, bin(n)[2:]))
elif num == 2:
    print('O número {} convertido para hexadecimal é: \n{}' .format(n, oct(n)[2:]))
else:
    print('O número {} convertido para octal é: \n{}' .format(n, hex(n)[2:]))
