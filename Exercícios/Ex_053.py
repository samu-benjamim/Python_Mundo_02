frase = str(input("Digite uma frase: ")).strip().upper()
palavra = frase.split()
junto = "".join(palavra)
inverso = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print("{} \n Temos um palíndromo". format(inverso))
else:
    print("{} \n Não é um palíndromo".format(inverso))