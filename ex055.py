pesos = []
for c in range(1, 6):
    peso = float(input('Informe o peso da {} pessoa:'.format(c)))
    pesos.append(peso)
print('O maior peso lido foi de {:.1f}Kg'.format(max(pesos)))
print('O menor peso lido foi de {:.1f}Kg'.format(min(pesos)))
