from _datetime import date
ano = int(input('Que ano você quer analisar? Coloque O para analisar o ano atual: '))
if ano == 0:
    # Utilizado para pegar o ano atual
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é Bisssexto!'.format(ano))
else:
    print('O ano {} não é Bissexto!'.format(ano))
