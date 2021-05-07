def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


lista = [0, 3, 4, 6, 1, 7]
dobra(lista)
print(lista)
