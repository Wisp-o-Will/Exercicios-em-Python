#Faça um Programa que peça a temperatura em graus Celsius, 
#transforme e mostre a temperatura em graus Fahrenheit.

Celsius = float(input("Informe o valor da temperatura a ser convertido(°C):"))
Farenheit = 1.8 * Celsius + 32

print(f"{Celsius}°C é igual a {Farenheit}°F")