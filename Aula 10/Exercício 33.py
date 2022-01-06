# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
from time import sleep
n1 = int(input('Dgite um número: '))
sleep(1)
n2 = int(input('Digite um segundo numero: '))
sleep(1)
n3 = int(input('Por fim digite um terceiro numero: '))
sleep(2)
# Verificando numero menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando numero maior 
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Os numeros digitados são:{}, {}, {}.'.format(n1, n2, n3))
sleep(1)
print('Sendo {} o numero maior e {} o numero menor.'.format(maior, menor))



