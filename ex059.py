n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor:'))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior 
    [ 4 ] Novos números 
    [ 5 ] Sair
    ''')
    opcao = int(input('Qual é a sua opção:'))
    if (opcao != 5):
        if opcao == 1:
            resultado = n1 + n2
            print('A soma entre {} + {} é {}'.format(n1, n2, resultado))
        elif opcao == 2:
            resultado = n1 * n2
            print('A soma entre {} x {} é {}'.format(n1, n2, resultado))
        elif opcao == 3:
            if n1 > n2:
                print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
            elif n1 < n2:
                print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
            else:
                print('Os valores são iguais')
        elif opcao == 4:
            print('Informe os números novamente:')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
        else:
            print('Opção inválida. Tente Novamente')
        print('=-' * 20)
print('Fim do Programa, volte sempre!')
