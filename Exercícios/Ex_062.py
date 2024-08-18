print("Gerador de uma PA")
print("=-"*15)
ter = int(input("\033[mPrimeiro termo da PA: \033[32m"))
raz = int(input("\033[mRazão da PA: \033[32m"))
n = 10
quantidade_termos = 0
while n != 0:
    c = 1
    while c <= n:
        if c == 1:
            res = ter
            print("\033[m{} -> ".format(res), end = "")
        else:
            res = ter + (raz * (c - 1))
            print("{} -> ".format(res), end = "")
        c += 1
    print("PAUSA")
    quantidade_termos += n
    n = int(input("Quantos termos você quer mostrar a mais? \033[32m"))
    ter = res + raz
print("\033[mProgressão finalizada com {} termos mostrados".format(quantidade_termos))        

          