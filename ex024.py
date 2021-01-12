cidade = str(input('Informe o nome da cidade: ')).strip()

# O strip elimina os espaços

primeiro = cidade.split()
if (primeiro[0].upper() == "SANTO"):
    print('True')
else:
    print('False')
