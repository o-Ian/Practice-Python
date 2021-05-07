exp = input('Digite um expressão matemática: ') .replace(' ', '')
pilha = []
for c in exp:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')
