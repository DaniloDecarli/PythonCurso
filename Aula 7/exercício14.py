# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em °C: '))
fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15
print('{}°C corresponde há: {}°F e {}K !'.format(celsius, fahrenheit, kelvin))

# Simplificado 
cel = float(input('Digite a temperatura em °C: '))
print('{}°C corresponde há: {}°F e {}K !'.format(cel, (celsius * 1.8) + 32, cel + 273.15))