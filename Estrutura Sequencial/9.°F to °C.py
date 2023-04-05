#Faça um Programa que peça a temperatura em graus Fahrenheit, 
#transforme e mostre a temperatura em graus Celsius.

Farenheit = float(input("Informe o valor da temperatura a ser convertido(°F):"))
Celsius = 5 * ((Farenheit-32) / 9)

print(f"{Farenheit}°F é igual a {Celsius:.2f}°C")