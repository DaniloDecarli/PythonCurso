# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0 # soma mais um valor ao outro
cont = 0 # adiciona mais um 
for c in range(1, 501, 2):
    if c % 3 == 0:
      soma = soma + c
      cont = cont + 1  
      print(c, end=' ')
print('\nA soma de todos os {} valores solicitados é: {}'.format(cont, soma))    