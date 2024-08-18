res = cont = 0
while True:
    n = int(input("Digite um número [999 para parar]: "))
    if n != 999:
        res += n
        cont += 1
    else:
        break
    
print("VocÊ digitou {} números e a soma entre ele foi {}.".format(cont, res))