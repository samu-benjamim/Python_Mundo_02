print("-" * 20)
print("LOJA SUPER BARATÃO")
print("-" * 20)
total = produto_caro = custo_p_barato = 0
while True:
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$ "))
    total += preco
    if preco > 1000.00:
        produto_caro += 1
    if custo_p_barato == 0 or preco < custo_p_barato: 
        custo_p_barato = preco
        produto_barato = produto
    esc = " "
    while esc not in "SN":
        esc = str(input("Quer continuar? [S / N] ")).upper().strip()   
    if esc == "N":
            break
print("-" * 10, "FIM DO PROGRAMA", ("-" * 10))
print(f"O total da compra foi R${total}")
print(f"Temos {produto_caro} produtos custando mais de R$1.000,00")
print(f"O produto mais barato foi {produto_barato} que custa R${custo_p_barato}")