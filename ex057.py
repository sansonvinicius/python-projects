sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]

while sexo not in 'MF':
    sexo = input('Dados Inválidos. Por favor, informe seu sexo:').strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))