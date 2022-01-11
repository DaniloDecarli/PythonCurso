# Programa que leia a idade e diga o tempo de alistamento militar

from time import sleep
from datetime import date
print('*' * 20, 'Programa de Alistamento', '*' * 20)
nome = str(input('Informe seu primeiro nome: '))
ano = int(input('Informe o ano de nascimento: '))
sleep(1)
idade = date.today().year - ano
if idade < 18:
    print('Faltam {} anos para seu alistamento.'.format(18 - idade))
elif idade > 18:
    print('Você já colaborou com nosso País Parabéns!!! está com {} anos'.format(idade)) 
else:
    print('Parabéns você está com {} anos, seu ano de alistamento! seja bem vindo recruta!'.format(idade))
print('-=-' * 60)           