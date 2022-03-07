# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint # Biblioteca para máquina escolher o número.
from time import sleep # Bibliotecca para processar "Efeito".
computador = randint(0, 10)
print('-=-' * 50)
sleep(1)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
sleep(1)
print('-=-' * 50 )
sleep(1)
print('Será que consegue adivinhar? ')
sleep(1)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Em que número eu pensei? ')) # JOgador tentar adivinhar.
    palpites = palpites + 1 
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Um pouco mais... Tente outra vez.')
        else:
            print('Um pouco menos... Tente outra vez.')       
print('Acertou! com {} palpites....'.format(palpites))  
                                                                    