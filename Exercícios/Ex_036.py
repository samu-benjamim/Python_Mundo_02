custo_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salário? "))
tempo_pagar = float(input("Quantos anos você deseja pagar? "))
parcela =  tempo_pagar * 12
parcela_custo = custo_casa / parcela
p30_salario = salario * (30/100)
if p30_salario <= parcela_custo:
    print("O empréstimo foi negado.")
else:
    print("O empréstimo foi aprovado\n Você deve para R${:.2f} em {} parcelas por mês".format(parcela_custo, parcela))