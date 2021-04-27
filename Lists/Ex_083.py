expre = ''
parenteses = 0
expre = (input('Digite um expressão: '))

if (expre.count('(')+expre.count(')')) % 2 == 0:
    print('A expressão é valida!')
else:
    print('A expressão não é válida!')
