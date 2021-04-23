f = input('Digite uma frase: ') .lower()
qntd_a = f.count('a')
first_a = f.find('a') + 1
last_a = f.rfind('a') + 1
print('Há {} "a" nessa frase.\nO número da posição do primeiro "a" é {}°.\nO número da posição do último "a" é {}°.' .format(qntd_a, first_a, last_a))
