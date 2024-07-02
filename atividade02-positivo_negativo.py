import os

os.system("cls")

numero = float(input("Digite um número: "))

if numero == 0:
    print("Esse número é 0")
elif numero < 0:
    print("Esse número é negativo")
else:
    numero > 0
    print("Esse número é positivo")
    