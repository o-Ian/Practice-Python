'''for c in range(0,9):
    print(c)
c = 0
while c <= 10:
    print(c)
    c += 1
s = 'S'
while s == 'S':
    n = int(input('Digite um número: '))
    s = input('Quer continuar? [S/N]: ') .upper()
print('FIM')'''
par = 0
impar = 0
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
print('Foram digitados {} números ímpares e {} números pares.' .format(impar, par))
