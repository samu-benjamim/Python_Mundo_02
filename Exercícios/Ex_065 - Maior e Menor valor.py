num = num_mais = num_menos = cont = cond = 0
while cond != 1:
    n = float(input("Digite um número: "))
    num += n
    if n > num_mais or num_mais == 0:
        num_mais = n
    if n < num_menos or num_menos == 0:
        num_menos = n
    cont += 1
    continua = str(input("Quer continuar? [S/N]")).upper(). strip()[0]
    if continua == "N":
        cond = 1
    else:
        cond = 0
print(f"Você digitou {cont} números e a média foi {num/cont:.2f}.")
print(f"O maior valor foi {num_mais:.0f} e o menor foi {num_menos:.0f}.")