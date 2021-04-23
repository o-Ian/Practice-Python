d1 = float(input('Digite o comprimento da reta A: '))
d2 = float(input('Digite o comprimento da reta B: '))
d3 = float(input('Digite o comprimento da reta C: '))
if d1 + d2 > d3 and d2 + d3 > d1 and d1 + d3 > d2:
    if d1 == d2 == d3:
        t = 'equilátero'
    elif d1 == d2 or d3 == d1 or d2 == d3:
        t = 'isósceles'
    else:
        t = 'escaleno'
    print('\033[1;42mÉ possível\033[m formar um triângulo {}!' .format(t))

else:
    print('\033[1;41mNão é possível\033[m formar um triângulo dado os comprimentos das retas ABC.')