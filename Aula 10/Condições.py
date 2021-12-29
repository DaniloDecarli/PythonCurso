# Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

nome = str(input('Qual é seu nome? '))
if nome == 'Danilo':
    print('Que nome lindo você tem!')
else:
    print('A sim legal!')    
print('Bom dia, {}!'.format(nome))    
print('Bom vamos verficar sua média!')
n1 = float(input('Digite sua primeira nota: '))   
n2 = float(input('Digite sua segundda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))
n5 = float(input('Digite sua quinta nota: '))
m = (n1 + n2 + n3 + n4 + n5)/5
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')