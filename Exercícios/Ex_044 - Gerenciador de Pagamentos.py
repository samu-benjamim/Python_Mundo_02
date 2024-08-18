print("=" * 10, "LOJAS SANTOS", "="*10)
valor = float(input("Preço das compras: "))
print("""FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opcao = input("Qual é a opção: ")
if opcao == "1":
    pag = valor - (valor * 0.10)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(valor, pag))
elif opcao == "2":
    pag = valor - (valor * 0.05)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(valor, pag))
elif opcao == "3":
    pag = valor 
    parc = valor / 2
    print("Sua compara de R${:.2f} será parcelada em 2x de R${:.2f} SEM JUROS".format(valor, parc))
elif opcao == "4":
    nparc = int(input("Quantas parcelas vai dividir?"))
    pag = valor + (valor * 0.20)
    parc = pag / nparc
    print("Sua compara será parcelada em {}x de R${:.2f} COM JUROS".format(nparc, parc))
    print("Sua compara de R${:.2f} vai custar R${:.2f} no final.".format(valor, pag))
else:
    print("Não Existe essa opção, tente novamente")
