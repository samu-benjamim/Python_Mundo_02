num = int(input("Digite um número inteiro: "))
print("""Escolha uma base para conversão
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL""")
esc = int(input("Qual sua escolha: "))
if  esc == 1:
    print("{} convertido para BINÁRIO é {}.".format(num, bin(num)[2:]))
elif esc == 2:
    print("{} convertido para OCTAL é {}.".format(num, oct(num)[2:]))
elif esc == 3:
    print("{} convertido para HEXADECIMAL é {}.".format(num, hex(num)[2:]))
else:
    print("Opção invalida")

