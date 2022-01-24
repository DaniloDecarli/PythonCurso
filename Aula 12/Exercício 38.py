# Programa que leia 2 numeros interios e diga qual é o maior, menor ou iguais.

from time import sleep
print('*' * 15,'\033[31mNúmeros\033[m', '*' * 15)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo numero: '))
if n1 > n2:
    print('O número \033[32m{}\033[m é maior!'.format(n1))
elif n1 < n2:
    print('O número \033[32m{}\033[m é maior!'.format(n2))
else:
    print('São iguais os numeros \033[32m{}\033[m!'.format(n1))