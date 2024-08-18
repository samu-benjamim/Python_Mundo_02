n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
med = (n1 + n2) /2
print("Tirando {} e  {}, a média do aluno é {}.".format(n1, n2, med))
if med < 5.0:
    print("O aluno está REPROVADO.")
elif 5.0 <= med < 6.9:
    print("O aluno está de RECUPERAÇÂO.")
else:
    print("O aluno foi APROVADO.")