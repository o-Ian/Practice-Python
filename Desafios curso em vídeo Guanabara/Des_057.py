'''s = 1
m = 0
f = 0
while s != '0':
	s = input('Digite o seu sexo\n[M] para masculino\n[F] para feminino\n>') .upper() .strip()
	if s == 'F' or s == 'M' or s == '0':
		if s == 'M':
			m += 1
		elif s == 'F':
			f += 1
	else:
		print('\033[1;41mVocê digitou algo inválido, tente novamente!\033[m')
print('Você digitou {} mulheres e {} homens.' .format(f, m))'''

sexo = input('Digite o seu sexo [M/F]: ').upper().strip()[0]
while sexo not in 'FM':
	sexo = input('Você digitou algo inválido, informe o sexo novamente: ') .upper() .strip()[0]
print('Sexo {} registrado com sucesso!' .format(sexo))
