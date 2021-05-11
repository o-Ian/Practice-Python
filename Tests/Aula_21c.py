def parOuimpar(num):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
print(parOuimpar(n))
