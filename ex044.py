preco_compra = float(input('Preço da Compra: R$'))
print('''FORMAS DE PAGAMENTO:
      [1] à vista dinheiro/cheque
      [2] à vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção?'))

if 0 < opcao < 5:
    if opcao == 1:
        preco_final = preco_compra - (preco_compra*0.1)
    elif opcao == 2:
        preco_final = preco_compra - (preco_compra*0.05)
    elif opcao == 3:
        parcela = preco_compra/2
        preco_final = preco_compra
        print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS'.format(parcela))
    elif opcao == 4:
        n_parcelas = int(input('Quantas parcelas?'))
        preco_final = preco_compra + (preco_compra*0.2)
        parcela = preco_final / n_parcelas
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(n_parcelas, parcela))

    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco_compra, preco_final))
else:
    print('Opção inválida! Escolha uma opção entre 1 e 4')
