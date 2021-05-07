l1 = float(input('Digite o comprimento da reta A: '))
l2 = float(input('Digite o comprimento da reta B: '))
l3 = float(input('Digite o comprimento da reta C: '))

if (l1 + l2) > l3 and (l2 + l3) > l1 and (l3 + l1) > l2:
    print('É possível formar um triângulo dado o comprimento dessas retas.')
else:
    print('Não é possível formar um triângulo dado o comprimento das retas.')
