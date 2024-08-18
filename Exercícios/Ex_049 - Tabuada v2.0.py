n = int(input("Digite um número para verificar sua taboada: "))
print("===============")
for i in range(1, 11):
    print("{:^3} x {:^3} = {:^3}".format(n, i, n*i))
print("===============")