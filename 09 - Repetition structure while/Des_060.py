from math import factorial

c = 0
while c < 10:
    n = int(input('Digite um número: '))
    print('O fatorial desse número é: {}' .format(factorial(n)))
    c += 1
print('FIM')
