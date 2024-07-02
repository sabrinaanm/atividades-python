import os

os.system("cls")

descrição = input("Descrição do produto: ")
quantidade = int(input("Quantidade do produto: "))
preco = float(input("Preço unitário: "))

total = quantidade * preco 

if quantidade <=5:
    total_desconto = total - (total * 2/100)
    print("O desconto será de 2% \n")
   
    
elif quantidade >5 and quantidade <= 10:
    total_desconto = total - (total * 3/100)
    print("O desconto será de 3% \n")


else:
    quantidade >10
    total_desconto = total - (total * 3/100)
    print("O desconto será de 5% \n")
   

print("Total com desconto: ", total_desconto)

input("Digite <ENTER> para continuar...")