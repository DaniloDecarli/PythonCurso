#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite um valor: '))
#s = n1 + n2
#print('A soma vale: ', s)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor: '))
s = n1 + n2
print('A soma entre {} e {} vale: {} !'.format(n1, n2, s))
#print('A soma entre: ', n1, 'e', n2, 'é:', s)

#nessa função ele me indica se for numero: True , caso seja palavra apresenta: False
n = input('Digite algo: ')
print(n.isnumeric()) 

#nessa função ele me indica se for palavra: True , caso seja numero apresenta: False
n3 = input('Digite algo: ')
print(n3.isalpha()) 

#nessa função ele me indica se for palavra e numero: True , caso seja caracteres apresenta: False
n4 = input('Digite algo: ')
print(n4.isalnum()) 

#nessa função ele me indica se for palavra com letras maiúscula: True , caso seja minúscula: False
n5 = input('Digite algo: ')
print(n5.isupper()) 