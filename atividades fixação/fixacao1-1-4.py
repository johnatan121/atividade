frutas = ["maçã", "banana", "laranja", "uva", "pera"]
while True:
    print("\nLista atual:", frutas)
    fruta = input("Digite uma fruta para adicionar: ")
    posicao = int(input("Digite a posição da fruta: "))
    frutas.append(fruta)
    escolha = input("Deseja adicionar mais frutas? (s/n): ").lower()
    if escolha == "n":
        break  
print("\nLista final de frutas:", frutas)
