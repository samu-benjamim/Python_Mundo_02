print("Vamos verificar quantos numeros pares existem entre 1 a 50")
inicio = str(input("Vamos iniciar S/N? "))
if inicio == "S":
    for i in range(2, 51, 2):
        print(i)
else: 
    print("Programa finalizado")