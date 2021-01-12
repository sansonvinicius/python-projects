n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2

if media < 5:
    situacao = 'REPROVADO'
elif media >= 5.0 and media < 7:
    situacao = 'RECUPERAÇÃO'
else:
    situacao = 'APROVADO'

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}\nO aluno está {}'.format(n1, n2, media, situacao))
