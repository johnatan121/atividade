velocidade = float(input("Informe a velocidade do carro em km/h: "))
velocidade_maxima = 80
excesso = velocidade - velocidade_maxima
print(f"\nVelocidade do motorista: {velocidade} km/h")
print(f"Velocidade máxima permitida: {velocidade_maxima} km/h")
if excesso <= 0:
    print("Situação: Dentro do limite. Nenhuma infração.")
    print("Pontos na carteira: 0")
elif excesso <= 10:
    print("Situação: Infração leve.")
    print("Pontos na carteira: 3")
elif excesso <= 20:
    print("Situação: Infração média.")
    print("Pontos na carteira: 4")
else:
    print("Situação: Infração grave.")
    print("Pontos na carteira: 7")