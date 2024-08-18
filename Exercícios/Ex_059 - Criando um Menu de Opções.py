from time import sleep
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
cond = 1
while cond != 0:
    print("=+="*15)
    sleep(2)
    print("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] novos números
[ 5 ] sair do programa""")
    esc = str(input("Qual é a sia opção?\n"))
    if esc == "1":
        res = num1 + num2
        print("A soma de {} + {} é {}.".format(num1, num2, res))
    elif esc == "2":
        res = num1 * num2
        print("A multiplicação de {} x {} é {}.".format(num1, num2, res))
    elif esc == "3":
        if num1 > num2:
            print("O maior numero é {}.".format(num1))
        elif num2 > num1:
            print("O maior numero é {}.".format(num2))
        else:
            print("O {} e {} são iguais.".format(num1, num2))
    elif esc == "4":
        num1 = int(input("Novo primeiro valor: "))
        num2 = int(input("Novo segundo valor: "))
    elif esc == "5":
        print("Obrigado por usar o programa. Até logo.")
        cond = 0
    else:
        print("Opção invalida tente novamento")

        
            
