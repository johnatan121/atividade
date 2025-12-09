start = int(input("Digite o valor inicial: "))
stop = int(input("Digite o valor final: "))
step = int(input("Digite o passo: "))
soma = 0
print("Sequência gerada:")
for numero in range(start, stop + 1, step):
    print(numero,)   
    soma += numero         
print(f"Soma dos números: {soma}")
