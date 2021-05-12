from Ex_107 import moeda
p = float(input('Digite o preço: '))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentado 10% de R${p} temos: R${moeda.aumentar(p, 10)}.')
print(f'Diminuindo 13% de R${p} temos: R${moeda.diminuir(p, 13)}.')
