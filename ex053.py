frase = input('Digite uma frase:').upper()
frase_sem_espaco = frase.replace(" ", "").upper()
invertida = frase_sem_espaco[::-1].upper() #para inverter a frase
print('O inverso de {} é {}'.format(frase_sem_espaco, invertida))
if frase_sem_espaco == invertida:
    print('Temos um palíndormo!')
else:
    print('A frase digitada não é um palíndormo!')