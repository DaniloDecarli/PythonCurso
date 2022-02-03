# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from time import sleep
from datetime import date
atual = date.today().year
print('Digite Sete anos de nascimentos...')
totMaior = 0
totMenor = 0
for p in range(1, 8):
    nasc = int(input('Em que ano nasceu a {}ª pessoa?:'.format(p)))
    idade = atual - nasc
    if idade >= 21:
        totMaior = totMaior + 1
    else:
        totMenor = totMenor + 1
print('''Ao todo são {} pessoas maiores de idade.
E {} pessoas são menores de idade.'''.format(totMaior, totMenor))