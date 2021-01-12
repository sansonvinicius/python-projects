import math
angulo = float(input('Informe o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O seno de {} é {:.2f},\no cosseno de {} é {:.2f} \ne a tangente de {:.2f} é {:.2f} '.format(angulo, seno, angulo, cosseno,
                                                                                     angulo, tangente), end="")

