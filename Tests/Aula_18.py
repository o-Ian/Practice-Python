test = []
test.append('Ian')
test.append(17)
galera = []
galera.append(test[:])
test[0] = 'Mário'
test[1] = 29
galera.append(test)
print(galera)