  # Programa que leia a idade e diga o tempo de alistamento militar

from time import sleep
from datetime import date
print('*' * 20, 'Programa de Alistamento', '*' * 20)
nome = str(input('Informe seu primeiro nome: '))
idade = int(input('Informe o ano de nascimento: '))
sleep(1)
liste = date.today().year - idade
if liste < 18:
    print('Faltam {} anos para seu alistamento {}.'.format((18 - liste), nome))
    print('Você se alistará em {}'.format((18 - liste) + (date.today().year)))
elif liste > 18:
    print('Você já colaborou com nosso País {} Parabéns!!! está com {} anos'.format(nome, liste)) 
    print('Você serviu ao País em {}'.format((date.today().year) - (liste - 18))) 
else:
    print('Parabéns {} você está com {} anos, esse é seu ano de alistamento! seja bem vindo recruta!'.format(nome, liste))
print('-=-' * 60)     