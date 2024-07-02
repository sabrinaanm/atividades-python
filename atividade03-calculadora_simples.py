import os

os.system("cls")

print("Calculadora Simples")

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

operacao = int(input("Digite 1 para Somar \n"
                 "Digite 2 para Subtrair \n"
                 "Digite 3 para Multiplicar \n"
                 "Digite 4 para Dividir \n"))

if operacao == 1:
    resultado = n1 + n2
elif operacao == 2:
    resultado = n1 - n2
elif operacao == 3:
    resultado = n1 * n2
else:
    resultado = n1 / n2

print("O resultado foi ", resultado)
