frase = str(input('Digite uma frase: ')).strip()
# para contar quantas vezes a letra a aparece. O lower() é para deixar tudo minusculo
# e contar mesmo que coloque A
print('A letra A aparece {} vezes na frase.'.format(frase.lower().count('a')))
# find() acha o primeira vez que o elemento apareceu e rfind() a última vez que o elemento apareceu
print('A primeira letra A aparece na posição {}'.format(frase.lower().find('a')+1))
print('A última letra A aparece na posição {}'.format(frase.lower().rfind('a')+1))

