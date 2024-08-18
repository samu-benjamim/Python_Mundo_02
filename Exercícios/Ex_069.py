pessoas_menos18 = homem = mulher_menos20 = 0
while True:
    print("-" * 20)
    print("CASTRE UMA PESSOA")
    print("-" * 20)
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M / F] ")).upper()
    print("-" * 20)
    if idade < 18:
        pessoas_menos18 += 1
    if sexo == "M":
        homem += 1
    if idade < 20 and sexo == "F":
        mulher_menos20 += 1
    esc = str(input("Quer continuar? [S/N] ")).upper()
    if esc == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {pessoas_menos18}")
print(f"Ao todo tem {homem} homens cadastrados.")
print(f"E temos {mulher_menos20} mulher com menos de 20 anos")
    