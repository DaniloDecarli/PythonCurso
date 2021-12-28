# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n =  str(input('Digite seu nome completo: ')).strip().upper()
nome = n.split() # A função split serve para fatiar(separar) o nomje do sobre nome.
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))