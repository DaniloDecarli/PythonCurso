nome = str(input('Qual é sue nome? '))
if nome == 'Danilo':
    print('Que nome bonito!')
elif nome == 'Glauco' or nome == 'Madureira':
    print('Que nome de boiola hem!')
elif nome in 'Fernanda Nair Heloisa Natalia':
    print('Que belo nome feminino!')
elif nome == 'Anderson':
    print('Você que domina isso tudo aqui!, é tudo seu !')        
else:
    print('Que nome comum...')
print('Tenha um bom dia {}!'.format(nome))            