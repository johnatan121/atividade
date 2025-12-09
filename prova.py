#cadastro_enem2025
#att 1 cadastro
cadastro_nome ='j'

cadastro_cpf = '731'

cadastro_senha = '0303'
cadastro_email = "j@2"
#att 2 acesso
email_aluno = input("digite seu e-mail; ")
aluno_senha = input("digite sua senha;")
if cadastro_email and email_aluno == aluno_senha and cadastro_senha:
         print("acesse liberado; ")
else:    
        print("acesso negado; ")

#att 3; lista com 3 curso        
lista=['matematica','ciencia','fisica']
lista.sort() 

#att 4 adicione    
lista.append('engenharia') 
print("Lista cursos:",lista)"""

#att 5 a nota
nota1 = int(input("digite sua nota linguagen, codigos; "))
nota2 = int(input("digiite sua nota matematica; "))
nota3 = int(input("digite sua nota ciencias da natureza: "))
nota4 = int(input("digite sua nota ciencias humanos; "))
nota5 = int(input("digite sua nota da redação; "))
soma= (nota1+nota2+nota3+nota4+nota5)
media = (soma /5)
print(f"sua nota {soma} sua media {media}")
#att 6
"""if media >= 450 and nota5 >=0:
    print("aluno apto a incrição ProUni:")
elif media <=450 and nota5 ==0:
    print(f"aluno nao apto media inferio a 450, media aluno; {media} redaçao zerado, nota redação; {nota5} ")
else: """
    #att 7
valor_curso = 1000

if media >= 701:
    print("bolsa 100%  ")
elif media >=651:     
    print(f"aluno ganhou 50% desconto; total com desconto: {valor_curso*0.5*48}")
elif media >= 601:
    print(f"aluno ganhou 40% desconto, total com desconto: {valor_curso*0.4*48}")  
elif media >= 551:
    print(f"aluno ganhou 35% desconto, total com desconto{valor_curso*0.35*48} ")    
elif media >= 451:
    print(f"aluno ganhou 30% desconto, total com desconto{valor_curso*0.30*48}")   
else:
    print(f"aluno ganhou 20% desconto {valor_curso*0.20*48}")  


