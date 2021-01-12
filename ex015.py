km = float(input('Quantidade de Km percorridos: '))
dias = int(input('Quantidade de dias: '))
preco = (60*dias)+(km*0.15)
print('O total a pagar é de R${:.2f}'.format(preco))
