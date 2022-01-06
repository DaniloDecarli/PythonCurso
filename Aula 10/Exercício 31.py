# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

from time import sleep # Bibliotecca para processar "Efeito".
print('Olá! Pronto para viajar?')
sleep(1)
distancia = float(input('Digite a distância em Km: '))
sleep(1)
print('Um momento, calculando sua passagem.......')
sleep(2)
print('Lembrando que o valor cobrado será de R$0,50 por Km para viagens até 200km e R$0,45 para as demais! ')
sleep(4)
if distancia <= 200:
    print('O valor de sua passagem é de:  R${:.2f}.'.format((distancia) * 0.50))
else:
    print('O valor da sua passagem é de: R${:.2f}.'.format((distancia) * 0.45))


