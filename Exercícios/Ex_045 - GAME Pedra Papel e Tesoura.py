from random import randint
from time import sleep
loop = True
while loop == True:
    print("Jogo Pedra, Pepel e Tesoura")
    print("""[0] Pedra
    [1] Papel
    [2] Tesoura
    [3] Sair""")
    opcoes = ("Pedra", "Papel", "Tesoura")
    esc = int(input("Qual sua escolha?"))
    esc_pc = randint(0,2)
    print("="*15)
    print("A escolha do computador foi {}".format(opcoes[esc_pc]))
    print("A sua escolha {}".format(opcoes[esc]))
    print("="*15)
    if esc_pc == 0:
        if esc == 0: 
            print("EMPATE")
        elif esc == 1:
            print("VOCÊ GANHOU") 
        elif esc == 2:
            print("O PC GANHOU")
        else: 
            print("FATAL ERRO")
    elif esc_pc == 1:
        if esc == 0:
            print("O PC GANHOU") 
        elif esc == 1:
            print("EMPATE")
        elif esc == 2:
            print("VOCÊ GANHOU") 
        else: 
            print("FATAL ERRO") 
    elif esc_pc == 2:
        if esc == 0:
            print("VOCÊ GANHOU") 
        elif esc == 1:
            print("O PC GANHOU") 
        elif esc == 2:
            print("EMPATE")
        else: 
            print("FATAL ERRO")
    if esc == 3:
        loop = False
        print("Foi bom jogar com você seu pato, sai dai e pede bença pro seu pai.")
