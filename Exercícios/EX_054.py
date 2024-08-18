from datetime import date
maior = 0
menor = 0
for i in range(1, 8):
    ano_nascimento = int(input("\033[m Em que ano a {}º pessoa nasceu? \033[32m".format(i)))
    idade = date.today().year - ano_nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print("\033[mAo todo tivemos {} pessoas maiores de idade".format(maior))
print("E também tivemos {} pessoas menores de idade".format(menor))

        
