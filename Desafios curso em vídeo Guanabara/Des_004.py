n = input('Digite algo: ')
cores = {'limpa' : '\033[m', 'amarelo': '033[33m', 'falsecor': '\033[1;40;31m', 'truecor': '\033[1;32;40m' }
print('O valor {} é do tipo {}.'.format(n, type(n)))
print('É formado somente por números? {}{}{}'.format(cores['falsecor'], n.isnumeric(), cores['limpa']))
print('É formado somente por letras? {}{}{}' .format(cores['truecor'], n.isalpha(), cores['limpa']))
print('É formado somente por espaços? {}{}{}'.format(cores['falsecor'], n.isspace(), cores['limpa']))
print('É formado por letras e números? {}{}{}' .format(cores['truecor'], n.isalnum(), cores['limpa']))
print('O valor é capitalizado? {}{}{}' .format(cores['falsecor'], n.istitle(), cores['limpa']))
