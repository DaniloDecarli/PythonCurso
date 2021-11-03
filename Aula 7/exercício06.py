#Crie uma algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Escreva um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O número que digitou é: {}, o seu dobro é: {}\nsendo: {} seu triplo, e sua raiz quadrada é {:.2f} '.format(n, d, t, r))


#método simplificado, com duas formas de calcular raiz quadrada (usando ** ou pow)
n1 = int(input('Escreva um numero: '))
#print('O numero qque digitou é: {}, o sue dobro é: {}\nsendo: {} seu triplo, e sua raiz quadrada é: {:.2f} '.format(n, (n * 2), (n * 3), (n ** (1/2))))
print('O numero qque digitou é: {}, o sue dobro é: {}\nsendo: {} seu triplo, e sua raiz quadrada é: {:.2f} '.format(n, (n * 2), (n * 3), pow(n,(1/2))))