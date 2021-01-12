from datetime import date
nascimento = int(input('Ano de nascimento:'))
ano_atual = date.today().year
idade = ano_atual - nascimento
ano_alistamento = nascimento + 18
sexo = input('Informe seu sexo: M para Masculino e F para feminino:').upper()


if sexo == 'M':
    if idade < 0:
        print('Você escolheu um ano futuro, escolha um ano até 2021')
    elif idade > 18:
        print('Você tem {} anos. Já se passaram {} anos da data do alistamento\nSeu alistamento deveria '
              'ter ocorrido em {}'.format(idade, ano_atual - ano_alistamento, ano_alistamento))
    elif idade < 18:
        print('Você tem {} anos.Ainda faltam {} anos para seu alistamento\nSeu alistamento será em {}'
              .format(idade, ano_alistamento - ano_atual, ano_alistamento))
    else:
        print('Você tem {} anos. Você deve se alistar em {}, é o ano exato para isso'.format(idade, ano_alistamento))

elif sexo == 'F':
    print('Pessoas do sexo FEMININO não são obrigadas a se alistar')
else:
    print('Valor incorreto, informe M ou F para o sexo')
