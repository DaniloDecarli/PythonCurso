# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint # Biblioteca para máquina escolher o número.
from time import sleep # Bibliotecca para processar "Efeito".
computador = randint(0, 5)
print('-=-' * 50)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 50 )
jogador = int(input('Em que número eu pensei? ')) # JOgador tentar adivinhar.
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número \033[31m{}\033[m e não no \033[33m{}\033[m!'.format(computador, jogador))
print('-=-' * 20 ,'FIM', '-=-' *20)    
