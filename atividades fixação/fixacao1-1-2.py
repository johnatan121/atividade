lista = []
i = 0
while i < 5:  
    numero = int(input(f"Digite o {i+1}º número: "))
    lista.append(numero)   
    i += 1                 
print("Lista completa:", lista)
maior = max(lista)
menor = min(lista)
soma = sum(lista)
media = soma / len(lista)
print("Maior número:", maior)
print("Menor número:", menor)
print("Soma:", soma)
print("Média:", media)
