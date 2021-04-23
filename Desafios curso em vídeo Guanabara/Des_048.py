s = 0
for c in range(1, 501, 2):
	if c % 3 == 0:
		s += c
print('A soma de todos os números ímpares que são múltiplos de 3 em um intervalo de 1 até 500 é {}.' .format(s))
