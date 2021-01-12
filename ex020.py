from random import shuffle
a1 = input('Informe o nome do 1 aluno: ')
a2 = input('Informe o nome do 2 aluno: ')
a3 = input('Informe o nome do 3 aluno: ')
a4 = input('Informe o nome do 4 aluno: ')
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('A lista sorteada foi: {} '.format(alunos))


