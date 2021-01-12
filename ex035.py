r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[0;33;45mOs segmentos acima PODEM formar um triângulo!\033[m')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')