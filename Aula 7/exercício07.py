#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.#

#Opção1
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
s = n1 + n2
m = s / 2
print('A soma de suas notas são: {}'.format(s))
print('Sendo assim sua média é: {}'.format(m))
#Opção2
n5 = float(input('Digite sua primeira nota: '))
n6 = float(input('Digite sua segunda nota: '))
m1 = (n5 + n6)/2
print('A soma de suas notas é: {}\nSendo assim sua média é: {}'.format((n5 + n6), (m1)))


#forma simplificada 
n3 = float(input('Digite uma nota: '))
n4 = float(input('Digite outra nota: '))
print('A soma de suas notas é: {}\nSendo assim sua média é: {}'.format((n3 + n4), ((n3 + n4)/2)))