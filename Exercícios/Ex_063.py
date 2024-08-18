print("-"*20)
print("Sequência de Fibinacci")
print("-"*20)
num = int(input("Quantos termos você quer mostrar?\033[32m"))
print("\033[m~"*(num*6))
a = 0 
b = 1
n = 1 
while n <= num:
    if n == 1:
        res = a
        print("{} ->".format(res), end = "")
        n += 1
    elif n == 2:
        res = b
        print(" {} ->".format(res), end = "")
        n += 1
    else:
        res = a + b
        print(" {} ->".format(res), end = "")
        n += 1
        a = b
        b = res
print(" FIM")
print("~"*(num*6))