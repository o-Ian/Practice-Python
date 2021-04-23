n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('Você foi \033[1;41mREPROVADO\033[m!')
elif media >=7:
    print('Você está em \033[1;42mAPROVADO\033[m!')
else:
    print('Você está de \033[1;43mRECUPERAÇÃO\033[m!')
