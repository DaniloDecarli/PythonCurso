#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
from time import sleep
print('\*/' * 20, 'Calcule seu IMC', '\*/' * 20)
sleep(1)
peso = float(input('Digite seu peso: (kg) '))
alt = float(input('Digite seu altura: (m) '))
sleep(1)
print('Processando...')
sleep(1)
imc = peso / (alt ** 2)
if imc <= 18.5:
    print('Seu IMC é {:.2f}, você está abaixo do peso!'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Seu IMC é {:.2f}, você está com peso Ideal! Parabéns!'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.2f}, você está com Sobrepeso!'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é {:.2f}, você está com Obesidade!'.format(imc))
else:
    print('Seu IMC é {:.2f}, você está com Obesidade Mórbida! Procure um médico....'.format(imc))    