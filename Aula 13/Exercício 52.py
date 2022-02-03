# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

from time import sleep
n = int(input('Digite um número inteiro: '))
sleep(0.5)
tot = 0
for c in range(1, n + 1): 
    if n % c == 0:
        print('\033[m', end=' ')
        tot = tot + 1
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end=' ')
print('\nO número \033[33m{}\033[m foi divisível \033[33m{}\033[m vezes'.format(n, tot))
sleep(1)    
if tot == 2:
    print('O número \033[33m{}\033[m é um número PRIMO!'.format(n))
elif tot == 1:
    print('O numero \033[33m{}\033[m não é um número PRIMO por que é divisível {} vez'.format(n, tot))    
else:
    print('O número \033[33m{}\033[m não é PRIMO por que é divisível \033[33m{}\033[m vezes'.format(n, tot))    