# Faça um programa que leia a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintalá-la, sabendo que cada litro pinta uma área de 2 metros quadrados.

larg = float(input('Digite o largura da Parede em metros: '))
alt = float(input('Digite a altura da Parede em metros: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))