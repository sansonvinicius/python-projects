from math import hypot
oposto = float(input('Informe a medida do cateto oposto: '))
adjacente = float(input('Informe a medida do cateto adjacente:'))
hipotenusa = hypot(oposto, adjacente)
print('O cateto oposto mede {:.2f}, o adjacente {:.2f} e a hipotenusa {:.3f}'.format(oposto, adjacente, hipotenusa))
