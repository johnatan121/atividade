n1 = float(input("digite a nota 1 bimestre "))
n2 = float(input("digite a nota 2 bimestre "))
n3 = float(input("digite a nota 3 bimestre "))
n4 = float(input("digite a nota 4 bimestre "))
media = (n1+n2+n3+n4)/4
print(f"media nota {media}")
if media>=6.0:
    print("aprovado")
elif media >= 5.0:
    print("recuperacao")   
else:
    print("reprovado")     