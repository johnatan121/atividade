nome_correto = "julia"
resposta = ""
while resposta != nome_correto:
    resposta = input("Qual é o meu nome? ")
    if resposta != nome_correto:
        print("Errado! Tente novamente...")
print("Parabéns, você acertou!")
