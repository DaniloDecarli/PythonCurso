# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

from math import trunc
num1 = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num1, trunc(num1)))

num2 = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num2, int(num2)))