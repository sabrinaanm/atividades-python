import os

os.system("cls")

nivel = int(input("Nível do Professor: "))
aula = int(input("Quantidade de aulas por semana: "))

if nivel == 1:
    salario = aula * 12
elif nivel == 2:
    salario = aula * 17
elif nivel == 3:
    salario = aula * 25
else:
    print("O nivel digitado é inválido")

input("Digite <ENTER> para continuar...")
