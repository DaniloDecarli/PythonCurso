#exercício 3
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor: '))
s = n1 + n2
print('A soma entre {} e {} vale: {} !'.format(n1, n2, s))

#exercício 4, vou criar um script que volta com todas a insformações sobre o que for digitado
a = input('Escreva algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaço? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúscula? ', a.islower())
print('Está capitalizada? ', a.istitle())
