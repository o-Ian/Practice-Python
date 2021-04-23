n = 'Ian'
print('Prazer, {}{}{}!!' .format('\033[7;30;46m', n, '\033[m'))
print('Prazer, {}{}{}!!' .format('\033[1;31m', n, '\033[m'))
cores = {'limpa' : '\033[m', 'amarelo' : '\033[33m', 'pretoebranco' : '\033[7;30m'}
print('Prazer, {}{}{}!!' .format(cores['amarelo'], n, cores['limpa']))