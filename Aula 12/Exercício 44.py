# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

produt = float(input('Digite o preço do produto desejado: R$ '))
print('Você escolheu um produto no valor de R$ {}'.format(produt))
print('''Escolha a forma de Pagamento:
[1] Á vista dinheiro/cheque
[2] Á vista no cartão
[3] Á prazo 2x no cartão
[4] Á prazo 3x ou mais no cartão ''')
opcao = int(input('Qual a forma de pagamento?: '))
if opcao == 1:
    print('O valor de R$ {:.2f}, a vista com 10% de desconto sai por R$ {:.2f} '.format(produt, (produt - (produt * 10/100))))
elif opcao == 2:
    print('O valor de R$ {:.2f}, a vista no cartão tem 5% de desconto e sai por R$ {:.2f}'.format(produt, (produt - (produt * 5/100))))
elif opcao == 3:
    print('O valor de R$ {:.2f}, a prazo em 2x no cartão sai pelo preço normal, com parcela no valor de R$ {:.2f}'.format(produt, (produt / 2)))
elif opcao == 4:
     print('O valor de R$ {:.2f}, a prazo em 3x ou mais  no cartão sai com 20% de juro no valor de R$ {:.2f}'.format(produt, (produt + (produt * 20/100))))
else:
    print('Opção inválida! tente novamente...')     