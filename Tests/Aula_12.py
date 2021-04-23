n = input('Digite o seu nome: ') .strip().title()
if n == 'Ian':
	print('Que nome bonito!')
elif n == 'Paulo' or n == 'Maria' or n == 'Luciana':
	print('Seu nome é bem normal!')
elif n in 'Ana Cláudia Paula Juliana':
	print('Belo nome feminino!')
else:
	print('Seu nome é feio!')
print('Seja bem vindo, {}!' .format(n))