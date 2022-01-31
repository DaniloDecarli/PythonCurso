# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.


numero =  int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = numero + (10 - 1) * razão
for c in range(numero, decimo + 1, razão):
    print('{} '.format(c), end=' ->')
print(' ->' * 3)
