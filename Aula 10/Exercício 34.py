# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
from time import sleep
print('Esse ano teremos reajuste Salárial!')
sleep(3)
salario = float(input('Digite seu Salário atual: R$ '))
sleep(1)
print('Processando....')
sleep(2)
if salario >= 1250:
    print('Com base no seu salário de R${:.2f}, você terá um aumento de 10%, agora seu salário será R$:{:.2f} '.format(salario, salario + (salario * 10 / 100)))
else:
    print('Com base no seu salário de R${:.2f}, você terá um aumento de 15%, agora seu salário será R$:{:.2f} '.format(salario, salario + (salario * 15 / 100)))

