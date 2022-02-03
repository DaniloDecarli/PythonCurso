# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
from time import sleep
frase = str(input('Digite uma frase: ')).strip().upper() #.strip é para tirar os espaços na frase / .upper deixa maiúscula
palavras = frase.split() # Divida as Palavras
junta =''.join(palavras)
inverso = ''
for letra in range(len(junta) - 1, -1, -1):
    inverso = inverso + junta[letra]
sleep (0.5)    
if inverso == junta:
    print('Temos um palíndromo!')
    print(junta, inverso)
else:
    print('A frase não é um palíndromo!') 
sleep(0.5)       
    
