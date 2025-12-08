compra = float(input("digite o valor da compra: "))
if compra >= 100:
    desconto = compra * 0.05
    total = compra - desconto
    print(f"desconto de 5% ja aplicado total; {total: .2f}")
else:
    print(f"nao tem desconto, total; {compra}")    
