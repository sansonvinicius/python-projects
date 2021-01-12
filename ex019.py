from random import choice
a1 = input('Informe o nome do aluno 1: ')
a2 = input('Informe o nome do aluno 2: ')
a3 = input('Informe o nome do aluno 3: ')
a4 = input('Informe o nome do aluno 4: ')
lista = [a1, a2, a3, a4]
sorteado = choice(lista)
print('O aluno sorteado foi {}'.format(sorteado))
