#Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.

nome = input("Olá, informe seu nome:")
ganho_hora = int(input("Informe quanto você gamha por hora:"))
horas_trabalho = int(input("Informe quantas horas você trabalhou esse mês:"))
salario = ganho_hora * horas_trabalho

print(f"Olá {nome}, de acordo com as informações, o seu salário será de R${salario}")