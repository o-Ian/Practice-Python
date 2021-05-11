def num():
    global x
    x = 3
    print(f'A variável X DENTRO vale {x}')

x = 2
num()

print(f'A variável X FORA vale {x}')