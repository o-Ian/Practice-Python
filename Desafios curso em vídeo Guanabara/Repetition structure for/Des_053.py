n = input('Digite uma frase ou palavra: ') .replace(' ', '') .lower()
menosn = n[::-1]
if menosn == n:
    print('Essa frase/palavra é um palíndromo.')
else:
    print('Essa frase/palavra não é um palíndromo.')
