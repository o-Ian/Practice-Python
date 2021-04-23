kmperco = float(input('Digite a quantidade de km que o carro percorreu: '))
d = int(input('Digite a quantidade de dias que você ficou com o carro: '))
print('O valor a pagar pelo carro é de R${:.2f}' .format(kmperco*0.15+d*60))
