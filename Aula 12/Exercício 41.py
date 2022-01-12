# Programa que leia idade e mostre categoria do atleta.
# até 9 anos mirim / até 14 infantil / até 19 junior / até 20 sênior / acima master.

from time import sleep
print('=' * 25, 'Campeonato de Natação', '=' * 25)
nome = str(input('Nome do atleta: '))
idade = int(input('Idade do atleta: '))
if idade <= 14:
    print('Atleta {}, categoria Infantil.'.format(nome))
elif idade > 15 and idade <= 19:
    print('Atleta {}, categoria Junior.'.format(nome))
elif idade == 20:
    print('Atleta {}, categoria Sênior.'.format(nome))
else:
    print('Atleta {}, categoria Master'.format(nome))            
