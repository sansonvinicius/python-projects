total_num = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        total_num += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(total_num, soma))
