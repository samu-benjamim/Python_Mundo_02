n = 0
res = 0
cont = 0
while n != 999:
    n = int(input("Digite um número [999 para parar]: "))
    res += n
    cont += 1
print("VocÊ digitou {} números e a soma entre ele foi {}.".format(cont - 1, res - 999))