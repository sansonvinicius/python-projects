salario = float(input('Qual é o salário do funcionário? R$'))
reajuste = salario+(salario*0.15)
print('Um funcionário que ganhava R$ {:.2f}, com o aumento de 15%, passa a receber R${:.2f}'.format(salario, reajuste))
