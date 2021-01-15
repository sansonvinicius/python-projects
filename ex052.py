n = int(input('Digite um número:'))
cont = 0
divisivel = []
for c in range(1, n+1):
    print(c, end=' ')
    if n % c == 0:
        cont += 1
        divisivel.append(c)

print('\nO número {} foi divisível {} vezes, por {}'.format(n, cont, divisivel))
if cont == 2:#se cont == 2 significa que ele é divisível só por 1 e ele mesmo
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')
