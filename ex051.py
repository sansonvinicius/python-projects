print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
ultimo = primeiro + (10-1) * razao #Porque pede os 10 primeiros termos

soma = 0
for c in range(primeiro, ultimo + razao, razao):
    print(c, end='->')
print('ACABOU')
