veloc = int(input('Informe a velocidade do carro: '))
multa = float(veloc - 80) * 7

if veloc > 80:
    print('MULTADO! Você excedeu o limite permitido, de 80 Km/h!\nVocê deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

