s1 = float(input("Primeiro segmento: "))
s2 = float(input("Segundo segmento: "))
s3 = float(input("Terceiro segmento: "))
list_s = [s1, s2, s3]
list_s.sort()
if list_s [0] + list_s [1] < list_s[2]:
    print("Os segmentos acima NÂO PODEM formar um triângulo")
else:
    if s1 == s2 == s3:
        print("Os segmentos acima PODEM formar um triângulo EQUILÁTERO") 
    elif s1 != s2 and s1 != s3:
        print("Os segmentos acima PODEM formar um triângulo ESCALENO")
    else:
        print("Os segmentos acima PODEM formar um triângulo ISÓCELES")