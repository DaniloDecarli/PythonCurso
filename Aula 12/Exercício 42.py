# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

from time import sleep
l1 = int(input('Informe um numero inteiro do lado A,B: '))
l2 = int(input('Informe um numero inteiro do lado B,C: '))
l3 = int(input('Informe um numero inteiro do lado C,A: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('As medidas {},{} e {} formam um triângulo!'.format(l1, l2, l3))
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')        
else:
    print('As medidas {}, {} e {} não formam um triângulo'.format(l1, l2, l3))
     
