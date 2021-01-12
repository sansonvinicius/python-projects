peso = float(input('Informe seu peso (kg):'))
altura = float(input('Informe sua altura (m):'))
imc = peso/(altura * altura)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso ideal!')
elif 18.5 <= imc < 25:
    print('Parabéns, você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com Sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com Obesidade!')
else:
    print('Cuidade, você está com Obesidade Mórbida!')
