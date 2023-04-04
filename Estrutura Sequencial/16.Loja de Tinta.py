'''
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

import math

#Tamanho da Área
tamanho_area = float(input("Informe o valor, em m², da área a ser pintada:"))

#Cobertura da Tinta
litros_necessarios = tamanho_area / 3

#Calculo de Galoes necessarios:
galoes_tinta = math.ceil(litros_necessarios / 18)
preço_galoes = galoes_tinta * 80

print(f'- Quantidade de Litros necessarios: {litros_necessarios}')
print(f'- Latas de tintas a serem compradas:{galoes_tinta}')
print(f'- Preço a ser pago:R${preço_galoes}')