n = int(input('Digite um número inteiro:'))
base = int(input('Escolha uma das bases para conversão: \n'
                 '[1] converter ara BINÁRIO\n'
                 '[2] converter para OCTAL\n'
                 '[3] converter para HEXADECIMAL\n'
                 'sua opção:'))
if base == 1:
    conversao = bin(n)
    tipo = 'BINÁRIO'
elif base == 2:
    conversao = oct(n)
    tipo = 'OCTAL'
elif base == 3:
    conversao = hex(n)
    tipo = 'HEXADECIMAL'
else:
    conversao = 0
    tipo = 'Valor Inválido, insira uma opçãp entre 1 e 3'

if base in range(1, 4):
    print('{} convertido para {} é igual a {}'.format(n, tipo, conversao[2:]))
else:
    print('Escolha um valor entre 1 e 3 para a base')



