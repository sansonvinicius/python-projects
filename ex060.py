'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial:'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

n = int(input('Digite um número para calcular seu Fatorial:'))
c = n
print('Calculando {}! = '.format(n), end='')
fatorial = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print('{}'.format(fatorial))
