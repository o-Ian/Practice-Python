d = float(input('Digite o total em Km da sua viagem: '))
if d<=200:
    print('Você pagará R${:.2f} por essa viagem.' .format(d*0.5))
else:
    print('Você pagará R${:.2f} por essa viagem.' .format(d*0.45))

'''preco = d*0.5 if d<= 200 else d*0.45
print(preco)'''