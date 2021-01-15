from datetime import date
soma_maior = 0
soma_menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu?'.format(c)))
    if date.today().year - ano > 18:
        soma_maior += 1
    else:
        soma_menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(soma_maior))
print('E também tivemos {} pessoas menores de idade'.format(soma_menor))
