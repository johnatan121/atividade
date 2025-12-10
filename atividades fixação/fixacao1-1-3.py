nomes = ["Ana", "Bruna", "julia", "Daniela", "jhennifer", "Fernanda"]
print("Lista inicial:", nomes)
posicao = int(input("Digite a posição (0 a 5) do nome que deseja remover: "))
del nomes[posicao]
print("Lista atualizada:", nomes)
