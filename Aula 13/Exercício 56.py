# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


somaIdade = 0
mediaIdade = 0
maiorIdadehomem = 0
nomeVelho = ''
totMulher20 = 0
nomeNova = ''
for p in range(1, 5):
    print('------- {}ª PESSOA -------'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaIdade = somaIdade + idade
    if p == 1 and sexo in 'Mm':
        maiorIdadehomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadehomem:
        maiorIdadehomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 = totMulher20 + 1    
        nomeNova = nome
mediaIdade = somaIdade / 4
print('A média de idadde do grupo é de {} anos.'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadehomem, nomeVelho))
print('E temos {} mulhere(s) com menos de 20 anos chamada {}.'.format(totMulher20, nomeNova))
print('-' * 40)