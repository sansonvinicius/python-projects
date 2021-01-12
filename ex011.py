altura = float(input('Informe a altura em metros: '))
largura = float(input('Informe a largura em metros: '))
area = altura * largura
litros_tinta = area/2

print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.2f} m2.\n Para pintar essa parede, '
      'você precisa de {:.2f} L de tinta'.format(altura, largura, area, litros_tinta))


