
from time import sleep
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p): # i: inicio f:fim p:de quantos em quantos pular
    print(c)
print('FIM')    

sleep(2)
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('O somatório de todos os valores foi {}'.format(s))    