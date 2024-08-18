print("=" * 12)
print("BANCO CEV")
print("=" * 12)
saque = int(input("Que valor você quer sacar? R$"))
restante = saque
if restante > 50:
    nota_50 = restante // 50
    print(f"Total de {nota_50} cédulas de R$50,00.")
    restante = saque % 50 
if restante > 20:
    nota_20 = restante // 20
    print(f"Total de {nota_20} cédulas de R$20,00.")
    restante = saque % 20
if restante > 10:
    nota_10 = restante // 10
    print(f"Total de {nota_10} cédulas de R$10,00.")
    restante = saque % 10  
if restante > 1:
    nota_1 = restante // 1
    print(f"Total de {nota_1} cédulas de R$1,00.")

    