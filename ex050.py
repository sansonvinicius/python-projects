soma = 0
cont = 0
lista = []
for c in range(1, 7):
    n = int(input('Informe o {} número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
        lista.append(n)
print('Os números pares da lista são {}'.format(lista))
print('Você informou {} números PARES e a soma é {}'.format(cont, soma))
