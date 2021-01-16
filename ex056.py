soma_idades = 0
cont_mulheres = 0
mais_velho = 0
nome_mais_velho = ''
for p in range(1, 5):
    print('-'*5, '{} PESSOA '.format(p), '-'*5)
    nome = input('Nome:')
    idade = int(input('Idade:'))
    sexo = input('Sexo [M/F]:').upper()
    soma_idades += idade


    if sexo == 'F' and idade < 20:
        cont_mulheres += 1

    if sexo == 'M' and p == 1:
        mais_velho = idade
        nome_mais_velho = nome

    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_mais_velho = nome

media_idades = soma_idades/4
print('A média de idades do grupo é de {:.1f} anos'.format(media_idades))
print('O homem mais velho tem {} anos e se chama {}'.format(mais_velho, nome_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont_mulheres))


