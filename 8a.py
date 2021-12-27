#from math import sqrt : nesse comando seleciono apenas uma função da biblioteca já  no debaixo importo toda biblioteca 
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a: {:.2f}'.format(num, raiz))


from math import sqrt
num1 = int(input('Digite um número: '))
raiz1 = sqrt(num1)
print('A raiz de {} é igual a: {:.2f}'.format(num1, raiz1))


from math import sqrt
num2 = int(input('Digite um número: '))
print('A raiz de {} é igual a: {:.2f}'.format(num2, sqrt(num2)))

# nessa função o programa me volta com numero aleatório 
import random
num3 = random.random()
print('Seu numero é: {}'.format(num3))
# Nessa função randint o programa alem de me voltar coom um numero aleatório inteiro também posso indicar até qual numero quero 
import random
num4 = random.randint(1, 10)
print('Seu numero é: {}'.format(num4))



