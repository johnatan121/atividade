nota1 = float(input('digite a nota do 1° bimestre; '))
nota2 = float(input('digite a nota do 2° bimestre; '))
nota3 = float(input('digite a nota do 3° bimestre; '))
nota4 = float(input('digite a nota do 4° bimestre; '))
media = (nota1+nota2+nota3+nota4)/4
if media >= 6:
    print(F"aprovado, sua media foi: {media:.2f}")
elif media >= 5:
    print(f"reprovado, sua media foi: {media:.2f}")  
else:
    print(f"reprovado sua media foi: {media:.2f}")      
