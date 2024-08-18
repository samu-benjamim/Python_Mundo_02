peso = float(input("Digite seu peso em quilogramas: "))
print(peso)
altura = float(input("Digite sua altura em metros: "))
print(altura)
res_imc = peso / (altura ** 2)
print(f"Seu IMC é: {res_imc} ")

if res_imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= res_imc < 24.9:
    print("Peso normal")
elif 24.9 <= res_imc < 29.9:
    print("Sobrepeso")
elif 30 <= res_imc < 39.9:
    print("Obesidade")
else:
    print("Obesidade mórbida")