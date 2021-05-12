from Ex_108 import moeda
p = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentado 10% de {moeda.moeda(p)} temos: {moeda.moeda(moeda.aumentar(p, 10))}.')
print(f'Diminuindo 13% de {moeda.moeda(p)} temos: {moeda.moeda(moeda.diminuir(p, 13))}.')
