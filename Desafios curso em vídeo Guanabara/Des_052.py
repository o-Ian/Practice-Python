divisores = 0
n1 = int(input('Digite um número inteiro: '))
for c in range(1, n1+1):
    if n1 % c == 0:
        divisores += 1
if divisores == 2:
    print('O número {} é primo!' .format(n1))
else:
    print('O número {} não é primo!' .format(n1))
