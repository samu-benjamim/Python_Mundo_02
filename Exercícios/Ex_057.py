i = 0
num_f = 0
num_m = 0
while i == 0:
    sexo = str(input("Qual o sexo[M/F]? ")).upper()
    if sexo == "F":
        num_f += 1
        i = 1
    elif sexo == "M":
        num_m += 1
        i = 1
    else: 
        print("Valor invalido tente novamente.")
        i = 0