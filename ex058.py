from random import randint
n = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

acertou = False
tentativas = 0

while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if n == palpite:
        acertou = True
    else:
        if n > palpite:
            print('Mais...Tente mais uma vez.')
        elif n < palpite:
            print('Menos...Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))

