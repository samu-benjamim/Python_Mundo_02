media_idade = 0
idade_acumulada = 0
h_velho = None
n_h_velho = 0
num_f_nova = 0
quant_f_nova = 20

for i in range(1, 5):
    print("\033[m-"*5," ", i,"º PESSOA ","-"*5 )
    nome = str(input("\033[m Nome: \033[32m")).strip()
    idade = int(input("\033[mIdade: \033[32m"))
    sexo = str(input("\033[mSexo [M/F]: \033[32m")).strip().upper()
    idade_acumulada += idade
    if sexo == "M" and n_h_velho < idade:
        n_h_velho = idade
        h_velho = nome
    if sexo == "F" and idade < quant_f_nova:
        num_f_nova += 1
media_idade = idade_acumulada / 4
print("\033[mA média de idade do grupo é de \033[44m{}\033[m anos".format(media_idade))
print("O homem mais velho tem \033[44m{}\033[m anos e se chama \033[44m{}\033[m".format(n_h_velho, h_velho))
print("Ao todo são \033[44m{}\033[m mulheres com menos de 20 anos".format(num_f_nova)) 
