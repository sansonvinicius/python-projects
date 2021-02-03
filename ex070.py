print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)

total = maior1000 = preco = 0
nome_menor = ' '

while True:
    continuar = ' '
    nome = input('Nome do Produto:')
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        maior1000 += 1
    if preco == total:
        menor = preco
        nome_menor = nome
    if preco < menor:
        menor = preco
        nome_menor = nome
    while continuar not in ('SN'):
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
print('--------- FIM DO PROGRAMA ----------- ')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {maior1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nome_menor} que custa R${menor:.2f}')