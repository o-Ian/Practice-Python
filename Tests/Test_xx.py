'''def num():
    global x
    x = 3
    print(f'A variável X DENTRO vale {x}')

x = 2
num()

print(f'A variável X FORA vale {x}')
n = '455B23'
a = ' '.join(n)
print(a)
print(a.split())'''
n = '45,34'
for c in n:
    if c.isalpha():
        print(c)