# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep # Bibliotecca para processar "Efeito".
velocidade = float(input('Digite sua velocidade: '))
multa = (velocidade - 79) * 7
print('Processando...')
sleep(3)
if velocidade <= 79:
    print('Boa viagem! não ultrapasse o limite da rodovia...')
else:
    print('Você foi multado em R${:.2F} por estar acima da velocidade permitida'.format(multa))
