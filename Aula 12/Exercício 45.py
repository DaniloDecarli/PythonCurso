# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha sua opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é sua jogada?: '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('-=' * 11)
print('Computador jogou: {}'.format(itens[computador]))
print('Jogador jogou: {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
   if jogador == 0:
       print('EMPATOU!')
   elif jogador == 1:
       print('JOGADOR GANHOU!')
   elif jogador == 2:
       print('COMPUTADOR GANHOU!')
   else :
       print('OPÇÃO INVÁLIDA!!!')        
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR GANHOU!')
    elif jogador == 1:
       print('EMPATOU!')
    elif jogador == 2:
        print('JAGADOR GANHOU!')
    else :
        print('OPÇÃO INVÁLIDA!!!')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR GANHOU!')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('EMPATOU!')
    else:
        print('OPÇÃO INVÁLIDA!!!')  
print('-=' * 11)                  