maior18 = 0
cont_homem = 0
cont_mulher_20 = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F]').upper().strip()[0]
    print('-' * 30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]').upper().strip()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade < 20:
        cont_mulher_20 += 1
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {cont_homem} homens cadastrados.')
print(f'E temos {cont_mulher_20} mulheres com menos de 20 anos.')
