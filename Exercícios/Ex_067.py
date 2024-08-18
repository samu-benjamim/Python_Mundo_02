while True:
    n = int(input("QUer ver a tabuada de qual valor? "))
    print("-" * 40)
    if n >= 0:
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
        print("-"*40)
    else:
        print("O programa foi ecerrado. Obrigado.")
        break