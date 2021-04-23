n = (int(input('Digite um valor: ')),
 int(input('Digite outro valor: ')),
 int(input('Digite mais um valor: ')),
 int(input('Digite o último valor: ')))

print(f'O número 9 apareceu {n.count(9)} vezes.')
if n.count(3) >= 1:
    print(f'Você digitou o número 3 na {n.index(3)+1}° vez.')
else:
    print('O número 3 não foi digitado nenhuma vez.')
print(f'Os números que foram digitados que são pares: ', end='')
for c in n:
    if c % 2 == 0:
        print(f'{c} ', end='')
