# Programa para aprovar empréstimo, onde leia o valor do imóvel, do salário, quantos anos quer pagar e calcular se o valor mensal não corresponde a mais que 30% do salário, caso contrário negar o empréstimo.

from time import sleep
print('-=-' * 20, 'Banco Central','-=-' *20)
print('*' * 5, 'Simulação de aquisição de Imóveis', '*' * 5)
sleep(1)
imovel = float(input('Digite o valor do imóvel: R$ '))
sleep(1) 
salario = float(input('Digite seu salário: R$ '))
sleep(1)
parcelas = int(input('Em quantos anos deseja pagar: '))
resultParcelas = imovel / (parcelas * 12)
margem = salario * 30/100
sleep(1)
print('Solicitado simulação de compra de imóvel no valor de R${:.2f} em {} anos, com parcelas no valor de R${:.2f}'.format(imovel, parcelas, resultParcelas))
print('Analisando...')
sleep(1)
if resultParcelas <= margem:
    print('Com base nos dados apresentado, seu emprestimo está APROVADO para confirmação!')
else:
    print('Com base nos dados apresentado o valor da parcela compromente mais de 30% de sua renda...')
    print('Emprestimo negado...')    
print('-=-' * 20, 'Banco Central','-=-' *20)
