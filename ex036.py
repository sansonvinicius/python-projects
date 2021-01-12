valor_casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o salário do comprador: R$'))
financiamento = int(input('Em quantos anos vai pagar:'))
prestacao = valor_casa/(financiamento*12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} '.format(valor_casa, financiamento,
                                                                                        prestacao))
if prestacao <= (salario*0.3):
    print('Empréstimo APROVADO')
else:
    print('Empréstimo NEGADO')