from datetime import date
nasc = int(input("Ano de nascimento: "))
ano_a = (date.today().year)
anos = ano_a - nasc
alis = nasc + 18
t_alis = alis - ano_a
print("Quem nasceu em {} tem {} anos em {}".format(nasc, anos, ano_a))
if alis > ano_a:
    print("Ainda faltam {} anos para o alistamento.\nSeu alistamento será em {} anos.".format(alis - ano_a, alis))
elif alis < ano_a:
    print("Você ja deveria ter se alistado há {}.\nSeu alistamento foi em {}.".format(ano_a - alis, alis))
else:
    print("Seu alistamento é esse ano. Boa sorte soldado.")