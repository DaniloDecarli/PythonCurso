#Faça um programa que leia um número e mostre na sua tela o seu sucessor e seu antecessor.

n = int(input('Escreve um número: '))
s = n + 1
b = n - 1
print('O numero que ecreveu é: {}, seu sucessor é: {}, e seu antecessor é: {}'.format(n, s, b))


#Forma mais simplificada 
n1 = int(input('Escreve um número: '))
print('O numero que ecreveu é: {}, seu sucessor é: {}, e seu antecessor é: {}'.format(n1, (n1 + 1), (n1 - 1)))