# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólres ela pode compra.

din = float(input('Digite quanto tem em dinheiro: R$ '))
dolar = din / 3.27
euro = din / 6.58
print('Você tem: R${:.2f} Reais podendo comprar: US$ {:.2f} Dólares, e {:.2f} € de Euro'.format(din, dolar, euro))