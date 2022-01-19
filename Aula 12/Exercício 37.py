# Programa que leia um numero inteiro e peça para escolher a base de conversão: binário, octal, hexadecimal.

from time import sleep
print('*' * 25, 'Conversor Numérico', '*' * 25)
numero = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
sleep(1)
opcao = int(input('Qula sua opção: '))
sleep(1)
if opcao == 1:
    print('O número {} convertido para BINÁRIO é igual a: {}'.format(numero, bin(numero)[2:])) #a opção 2: serve para tirar as duas letras iniciais que aparece e não quero ver
elif opcao == 2:
    print('O número {} conertido para OCTAL é igual a: {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é igual a: {}'.format(numero, hex(numero)[2:]))
else:
    print('''Opção Inválida!
Tente novamente!''')
