# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.


num = int(input('Digite um numero para ver sua tabuada : '))
print('=' * 15)
for c in range(1, 11):
    print('{} x {} = {}'.format(c, num, c * num))
print('=' * 15)