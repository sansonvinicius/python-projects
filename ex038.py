n1 = int(input('Informe o primeiro número:'))
n2 = int(input('Informe o segundo número'))

if n1 > n2:
    print('o primeiro valor: {} é maior que o segundo: {}'.format(n1, n2))
elif n2 > n1:
    print('o segundo valor: {} é maior que o primeiro: {}'.format(n2, n1))
else:
    print('Não existe valor maior, os dois são iguais')
