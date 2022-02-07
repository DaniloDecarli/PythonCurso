# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print('Digite o peso de cinco Pessoas...')
for p in range(1, 6):
    peso = float(input('Digite o {}º peso: '.format(p)))