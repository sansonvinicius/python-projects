continuar = 'S'
soma = 0
cont = 0
maior = menor = 0

while continuar in 'Ss':
    n = int(input('Digite um número:'))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = input('Quer continuar? [S/N]').upper().strip()[0]
media = soma/cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O Maior valor foi {} e o menor valor foi {}'.format(maior, menor))


