from random import randint
print("=-" * 20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 20)
cont = 0
while True:
    num_pc = randint(1, 10)
    num = int(input("Digite um número: "))
    escolha = str(input("Par ou ímpar? [P/I] ")).upper().strip()
    soma = num + num_pc
    if escolha == "P":
        res = "PAR" 
    elif escolha == "I":
        res = "ÍMPAR"
    print("-" * 40)
    print(f"Voce jogou {num} e o computador {num_pc}. Total de {soma} DEU {res}")
    print("-" * 40)
    if soma % 2 == 0 and escolha == "P":
        print("Você VENCEU")
        print("=-" * 20)
        cont += 1
    elif soma % 2 == 1 and escolha == "I":
        print("Você VENCEU")
        print("=-" * 20)
        cont += 1
    else:
        print("Você PERDEU!")
        print(f"GAME OVER! Você venceu {cont} vezes.")
        break
    
    