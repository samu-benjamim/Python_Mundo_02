peso_maior = None
peso_menor = None
for i in range(1, 6):
    peso = float(input("\033[mPeso da {}º pessoa:\033[32m ".format(i)))
    if peso_maior is None or peso > peso_maior:
        peso_maior = peso
    if peso_menor is None or peso < peso_menor:
        peso_menor = peso
print("\033[mO maior peso lido foi de {}Kg".format(peso_maior))
print("O menor peso lido foi de {}Kg".format(peso_menor))