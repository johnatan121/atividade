compra = float(input("Informe o valor da compra: R$ "))

if compra >= 500:
    print("Você ganhou frete grátis e um brinde!")
elif compra >= 200:
    print("Você ganhou frete grátis!")
elif compra >= 50:
    print("O valor do frete é R$ 20,00.")
else:
    print("O valor do frete é R$ 10,00.")
