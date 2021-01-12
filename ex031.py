distancia = float(input('Informe a distância da viagem em Km: '))

print('Você está prestes a começar uma viagem de {} Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print('O preço da passagem será R$ {:.2f}'.format(preco))
