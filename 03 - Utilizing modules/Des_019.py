from random import choice
a1 = str(input('Digite o nome do aluno 1: '))
a2 = str(input('Digite o nome do aluno 2: '))
a3 = str(input('Digite o nome do aluno 3: '))
a4 = str(input('Digite o nome do aluno 4: '))
lista_alunos = [a1, a2, a3, a4]
print('O aluno escolhido foi {}.' .format(choice(lista_alunos)))
