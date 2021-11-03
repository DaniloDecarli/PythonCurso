# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite a medida em metros: '))
mc = n * 1000
ml = n * 10000
print('A medida que digitou é de: {} metros, que é o equivalente a: {} centímetros, e: {} milímetros '.format(n, mc, ml))

n1 = float(input('Digite a medida em metros: '))
print('A medida que digitou é de: {} metros, que é o equivalente a: {} centímetros, e: {} milímetros '.format(n1, (n1 * 1000), (n1 * 10000)))


#completa 
metros = float(input('Digite a medida em metros: '))
print('A medida que informou é de: {} metros e pode ser convertida em:\n{} Quilômetro\n{} Centímetro\n{} Milímetro\n{} Milha '.format(metros, (metros / 1000), (metros * 100), (metros * 1000), (metros / 1609)))
