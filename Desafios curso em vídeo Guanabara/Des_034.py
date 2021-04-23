s = float(input('Digite o valor de seu salário em R$: '))
if s>1250:
    print('Seu salário teve um aumento de 10% e foi para R${:.2f}' .format(s*1.1))
else:
    print('Seu salário teve um aumento de 15% e foi para R${:.2f}' .format(s*1.15))