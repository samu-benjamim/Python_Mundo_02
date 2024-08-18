print("Gerador de uma PA")
print("=-"*15)
ter = int(input("\033[mPrimeiro termo da PA: \033[32m"))
raz = int(input("\033[mRazão da PA: \033[32m"))
c = 1
while c <= 10:
    if c == 1:
        res = ter
        print("\033[m{} -> ".format(res), end = "")
    else:
        res = ter + (raz * (c - 1))
        print("{} -> ".format(res), end = "")
    c += 1
print("FIM")
        

          
