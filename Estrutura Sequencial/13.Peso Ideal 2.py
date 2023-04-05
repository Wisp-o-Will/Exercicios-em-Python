#Construa um algoritmo que calcule seu peso ideal.

#Informações Pessoais
genero = input("Informe seu genero:")
altura = float(input("Informe sua altura em M:"))
peso = float(input("Informe seu peso em Kg:"))

#Calculo de Peso Ideal para Homens e Mulheres
if genero == 'Homem':
    peso_ideal = (72.7 * altura) - 58

elif genero == 'Mulher':
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Inválido")

print(f"De acordo com as informações fornecidas, o seu peso ideal é {peso_ideal:.2f}kg")