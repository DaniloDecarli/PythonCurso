# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

from time import sleep
print('-=-' * 50)
print('ANALIZANDO TRIÂNGULO')
print('-=-' * 50)
r1 = float(input('Informe a primeira medida: '))
r2 = float(input('Informe a segunda medida: '))
r3 = float(input('Informe a terceira medida: '))
sleep(1)
print('Processando...')
sleep(2)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As medidas {},{} e {} formam um triângulo!'.format(r1, r2, r3))
else:
    print('As medidas {}, {} e {} não formam um triângulo'.format(r1, r2, r3))