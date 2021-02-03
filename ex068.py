from random import randint
print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)

venceu = True
total_vitorias = 0

while True:
    escolha = ' '
    if venceu == False:
        break

    computar = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    while escolha not in 'PI':
        escolha = input('Par ou Ímpar? [P/I]').upper().strip()[0]
    resultado = (jogador + computar) % 2

    if escolha == 'P' and resultado == 0:
        venceu = True
        par_impar = 'Par'
        total_vitorias += 1
    elif escolha == 'P' and resultado == 1:
        venceu = False
        par_impar = 'Ímpar'
    elif escolha == 'I' and resultado == 1:
        venceu = True
        par_impar = 'Ímpar'
        total_vitorias += 1
    elif escolha == 'I' and resultado == 0:
        venceu = False
        par_impar = 'Par'
    print('-'*40)
    print(f'Você escolheu {jogador} e o computador {computar}. Total de {jogador+computar} DEU {par_impar}.')
    print('-' * 40)

    if venceu == True:
        print('Você VENCEU!\nVamos jogar novamente...')
        print('-=' * 20)
print('Você PERDEU!')
print('-='*20)
print(f'GAME OVER! Você ganhou {total_vitorias} vezes.')
