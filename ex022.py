nome = str(input('Digite seu nome completo: ')).strip()
maiuscula = nome.upper()
minuscula = nome.lower()
total_letras = len(nome)-nome.count(' ')
primeiro = nome.split()

print('Analisando seu nome... \nSeu nome em maíusculas é {}'
      '\nSeu nome em minusculas é {}\nSeu nome tem ao todo {} letras\n'
      'Seu primeiro nome é {} e ele tem {} letras'
      .format(maiuscula, minuscula, total_letras, primeiro[0], len(primeiro[0])))
