from random import randint
n = randint(0, 5)
tentativa = int(input('Informe um número entre 0 e 5: '))
print('PROCESSANDO:')
print('O número escolhido pelo computador foi: {}'.format(n))
print('O número que você escolheu foi: {}'.format(tentativa))
if n == tentativa:
    print('Você GANHOU!!!')
else:
    print('Você PERDEU')
