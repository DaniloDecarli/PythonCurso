#for c in range(1,11):
#    print(c)
#print('---Fim---')    

c = 1
while c < 11:
    print(c)
    c = c + 1
print('---Fim---')    

r = 'S'
soma = 0
while r == 'S':
    n = int(input('Digitte um valor: '))
    r = str(input('Quer continuar?[S/N]')).upper() #upper joga o s para S.
    soma = soma + n
print(soma)     
print('---Fim---')    