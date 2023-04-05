'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados :
- 11% para o Imposto de Renda
- 8% para o INSS 
- 5% para o sindicato
'''

#Ganho por hora e hora trabalhada:
ganho_hora = float(input("Informe quanto você ganha por hora:"))
horas_trabalho = float(input("Informe quantas horas você trabalhou esse mês:"))

#Salario Bruto:
salario_bruto = ganho_hora * horas_trabalho

#INSS:
inss = salario_bruto * 0.08

#Sindicato:
sindicato = salario_bruto * 0.05

#Imposto de Renda:
imposto_renda = salario_bruto * 0.11

#Roubo:
roubo = inss + sindicato + imposto_renda

#Salario Liquido:
salario_liquido = salario_bruto - roubo

print(f"- Salario Bruto:R${salario_bruto}")
print(f"- INSS:R${inss}")
print(f"- Sindicato:R${sindicato}")
print(f'- Imposto de Renda:R${imposto_renda}')
print(f'- Desconto total:R${roubo}')
print(f'- Salario Liquido:R${salario_liquido}')


