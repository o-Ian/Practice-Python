p = float(input('Digite o preço do produto: '))
pag = int(input('Qual será a forma de pagamento?\n'
                'Digite 1 para pagar à vista no dinheiro ou cheque.\n'
                'Digite 2 para pagar à vista no cartão.\n'
                'Digite 3 para pagar em 2x no cartão.\n'
                'Digite 4 para pagar em 3x ou mais no cartão.\n'))
if pag == 1:
    print('Você pagará um valor total de R${:.2f}' .format(p*0.9))
elif pag == 2:
    print('Você pagará um valor total de R${:.2f}' .format(p*0.95))
elif pag == 3:
    print('Você pagará 2 parcelas de R${:.2f}, o valor total ficará em R${:.2f}.' .format(p/3, p))
elif pag == 4:
    print('Você pagará um valor total de R${:.2f}.' .format(p*1.2))
else:
    print('\033[31mDigite um número válido!\033[m')