num = []
for c in range(0, 5):
    n = (int(input('Digite um valor: ')))
    if c == 0 or n>= max(num):
        print('Adicionando ao final da lista!')
        num.append(n)
    elif n <= min(num):
        print('Adicionando na posição 0 da lista!')
        num.insert(0, n)
    if min(num) < n < max(num):
        if n <= num[4]:
            num.insert(4, n)
            print('Adicionando na posição 4')
            if n <= num[3]:
                num.insert(3, n)
                print('Adicionando na posição 3')
                if n <= num[2]:
                    num.insert(2, n)
                    print('Adicionando na posição 2')
                    if n <= num[1]:
                        num.insert(1, n)
                        print('Adicionando na posição 1')
print(num)