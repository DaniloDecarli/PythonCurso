nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Digíte um valor: '))
n2 = int(input('Digíte outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é: {}, o multiplicação é: {}, \n a divisão é: {}, a divisão interia é: {}, \n e a potência é: {}'.format(s, m, d, di, e))