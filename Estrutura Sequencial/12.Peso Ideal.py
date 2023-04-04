#Tendo como dados de entrada a altura de uma pessoa,
#construa um algoritmo que calcule seu peso ideal.

nome = input("Olá, informe seu nome:")
altura = float(input("Informe sua altura em M:"))
peso = float(input("Informe seu peso em Kg:"))

peso_ideal = (72.7 * altura) - 58

print(f"{nome}, de acordo com as informações fornecidas, o seu peso ideal é {peso_ideal:.2f}kg")