from random import randint
print('''Suas opções:
        [0] PEDRA
        [1] PAPEL
        [2] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
computador = randint(0, 2)

if computador == 0 and jogador == 1:
    print('O computador jogou PEDRA e você jogou PAPEL, VOCÊ VENCEU!')
elif computador == 0 and jogador == 2:
    print('O computador jogou PEDRA e você jogou TESOURA, VOCÊ PERDEU!')
elif computador == 1 and jogador == 0:
    print('O computador jogou PAPEL e você jogou PEDRA, VOCÊ PERDEU!')
elif computador == 1 and jogador == 2:
    print('O computador jogou PAPEL e você jogou TESOURA, VOCÊ VENCEU!')
elif computador == 2 and jogador == 0:
    print('O computador jogou TESOURA e você jogou PEDRA, VOCÊ VENCEU!')
elif computador == 2 and jogador == 1:
    print('O computador jogou TESOURA e você jogou PAPEL, VOCÊ PERDEU!')
elif computador == jogador:
    print('EMPATE')
else:
    print('Jogada inválida, escolha um número de 0 a 2!')
print(jogador,computador)

