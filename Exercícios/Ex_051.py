print("="*20)
print("10 TERMO DE UMA PA")
print("="*20)
pt = int(input("Qual o primeiro Termo: "))
razao = int(input("Qual a razão: "))
decimo = pt +(10 - 1) * razao
for i in range(pt, decimo + razao, razao):
    print("{}".format(i), end=" ->")
print("ACABOU")


