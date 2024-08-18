from random import randint
from time import sleep
jogo = True
tentativas = 0
while jogo == True:
    print("\033[33m-=-\033[m"*40)
    print("\033[34mVou pensar em um número entre 0 a 10. Tente adivinhar....\033[m")
    print("\033[33m-=-\033[m"*40)
    num = int(input("Em que número eu pensei? \n\033[32m"))
    print("\033[35mPROCESSANDO...\033[m")
    sleep(1)
    escolha = randint(0, 11)
    if escolha == num:
        print("\033[32mPARABÉNS! Você conseguiu me vencer!\033[m")
        tentativas += 1
        jogo = False
    else:
        print("{}GANHEI! Eu pensei no número {} e não no {}!{}".format("\033[31m", escolha, num, "\033[m"))
        tentativas += 1
print("Você tentou {} vezes até acertar".format(tentativas))