from datetime import date
nascimento = int(input('Informe o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

if nascimento <= ano_atual:

    if idade <= 9:
        classificacao = 'MIRIM'
    elif idade <= 14:
        classificacao = 'INFANTIL'
    elif idade <= 19:
        classificacao = 'JUNIOR'
    elif idade <= 25:
        classificacao = 'SÊNIOR'
    else:
        classificacao = 'MASTER'

    print('O atleta tem {} anos\nClassificação:{}'.format(idade, classificacao))

else:
    print('Você informou um ano futuro, informe um ano até {}'.format(ano_atual))



