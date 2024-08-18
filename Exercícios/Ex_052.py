number = int(input("Digite um número: "))
tot = 0
for i in range (1, number+1):
    if number % i == 0:
        print("\033[33m", end = "")
        tot += 1
    else:
        print("\033[31m", end = "")
    print("{} ".format(i), end="")
print("\n\033[mO número {} foi dividsivel {} vezes".format(number, tot))
if tot == 2:
    print("E por isso ele É PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")