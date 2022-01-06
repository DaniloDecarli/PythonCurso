# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from time import sleep
from datetime import date
print('Olá você sabe quais são os anos Bissexto?')
sleep(2)
ano = int(input('Bom posso te ajudar! Digite qual ano que deseja saber ou digite 0 para seu ano atual: '))
sleep(1)
print('Processando...')
sleep(1)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÂO é BISSEXTO.'.format(ano))
 
