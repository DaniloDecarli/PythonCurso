# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

'''import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno  = math.sin(math.radians(angulo))
print('O ângulo de {} tem o Seno de: {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o Cosseno: {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a Tangente: {:.2f}'.format(angulo, tangente))'''

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o Seno: {:.2f} \nO Cosseno: {:.2f} \nA Tangente: {:.2f}'.format(angulo, seno, cosseno, tangente))