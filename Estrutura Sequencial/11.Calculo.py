#Faça um Programa que peça 2 números inteiros e um número real.
inteiro1 = int(input("Informe o primerio numero inteiro:"))
inteiro2 = int(input("Informe o segundo numero inteiro:"))
real = float(input("Informe um numero real:"))

#O produto do dobro do primeiro com metade do segundo.
calculo_1 = (inteiro1 * 2) + (inteiro2 / 2)

#A soma do triplo do primeiro com o terceiro.
calculo_2 = (inteiro1 * 3) + real

#O terceiro elevado ao cubo.
calculo_3 = real**3

print(f"A.O produto do dobro do primeiro com metade do segundo. {calculo_1}")
print(f"B.A soma do triplo do primeiro com o terceiro. {calculo_2}")
print(f"C.O terceiro elevado ao cubo. {calculo_3}")