# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Quantos dias permaneceu com o veículo? : '))
k = float(input('Quantos Km foram percorridos? : '))
dias = d * float (60.00)
km = k * 0.15
diarias = dias + km
print('Você permaneceu com o veículo por {} dias, valor de R${:.2f}\nE percorreu {}Km, valor de R${:.2f}\nSomando um total de R${:.2f} do aluguel a ser pago.'.format(d, dias, k, km, diarias))

# Simplificado
d1 = int(input('Quantos dias permaneceu com o veículo? : '))
k1 = float(input('Quantos Km foram percorridos? : '))
print('Você permaneceu com o veículo por {} dias, valor de R${:.2f}\nE percorreu {}Km, valor de R${:.2f}\nSomando um total de R${:.2f} do aluguel a ser pago.'.format(d1, d1 * float(60.00), k1, k1 * 0.15, d1 * float(60.00) + k1 * 0.15))

