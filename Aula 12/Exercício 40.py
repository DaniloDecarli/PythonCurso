# Programa que lei duas notas, calcule a média e diga se está aprovadado.
# 4.9 pra baixo reprovado / 5.0 a 6.9 recuperação / acima de 7.0 aprovado

from time import sleep
print('*+*' * 20, 'Conferencia de notas', '*+*' * 20)
n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua primeira segunda: '))
n3 = float(input('Informe sua primeira terceira: '))
media = (n1 + n2 + n3) / 3
if media >= 7.0:
    print('Sua média é:{:.2f}'.format(media))
    print('Parabéns você foi aprovado!')
elif media >= 5.0 and media <= 6.9:
    print('Estude um pouco mais sua média é {:.2f}, você está de recuperação.'.format(media))
else:
    print('Estude mais você foi reprovado, sua nota é {:.2f}'.format(media))