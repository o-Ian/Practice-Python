expre = []
parenteses = 0
expre.append(input('Digite um expressão: '))
for c in expre:
    if c in '()':
        parenteses += 1
print(parenteses)