'''
Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
'''

import math

print("Olá, seja bem-vindo. De qual forma você gostaria de comprar tinta?")
print("1 - Comprar apenas Latas de 18L")
print("2 - Comprar apenas Galões de 3.6L")
print("3 - Misturar Latas e Galões")

escolha = int(input("Informe sua escolha:"))

tamanho_area = float(input("Informe o valor, em m², da área a ser pintada:"))
tinta_necessaria = (tamanho_area / 6)
latas = math.ceil(tinta_necessaria / 18)
galoes = math.ceil(tinta_necessaria / 3.6)

print(f'Quantidade de tinta necessária:{tinta_necessaria:.2f}l')

#Comprar apenas Latas:
if escolha == 1:
    preço_latas = latas * 80
    print(f'- Você optou por comprar apenas Latas de 18l')
    print(f'- Latas necessárias: {latas}')
    print(f'- Preço: R${preço_latas}')

#Comprar apenas Galões:
elif escolha == 2:
    preço_galoes = galoes * 25
    print(f'- Você optou por comprar apenas Galões de 3.6L')
    print(f'- Galões necessários: {galoes}')
    print(f'- Preço: R${preço_galoes}')

#Comprar Latas e Galões:
elif escolha == 3:
    latas_inteiras = math.floor(tinta_necessaria / 18)
    tinta_restante = tinta_necessaria % 18
    galoes_inteiros = math.ceil(tinta_restante / 3.6)

    if galoes_inteiros == 5:
        galoes_inteiros == 0
        latas_inteiras += 1

    preço_latas_inteiras = latas_inteiras * 80
    preço_galoes_inteiros = galoes_inteiros * 25

    preço_mistura = preço_galoes_inteiros + preço_latas_inteiras

    print(f'- Você optou por comprar Latas e Galões.')
    print(f'- Latas necessárias:{latas_inteiras}')
    print(f'- Galões necessários:{galoes_inteiros}')
    print(f'- Preço da mistura:R${preço_mistura}')

else:
    print('Opção Invalida')