import math

#entrada 
lado01 = float(input("Digite o valor do primeiro lado do terreno (m): "))
lado02 = float(input("Digite o valor do segundo lado do terreno (m): "))
lado03 = float(input("Digite o valor do terceiro lado do terreno (m): "))
lado04 = float(input("Digite o valor do quarto lado do terreno (m): "))

mourao = int(input("Digite o valor do mourão: "))
arame = float(input("Digite o valor do arame por metro: "))

#processamento
terreno = lado01 + lado02 + lado03 + lado04
mourao_necessario = math.ceil(terreno / 3) 
arame_necessario = terreno * 4

valor_mourao = mourao_necessario * mourao
arame_total = arame_necessario * arame
preco = valor_mourao + arame_total


# saída
print(f"\nNúmero de mourões necessários: {mourao_necessario}")
print(f"Valor gasto com mourão: R$ {valor_mourao:.2f}")
print(f"Valor gasto com arame: R$ {arame_total:.2f}")
print(f"Valor total para cercar o terreno: R$ {preco:.2f}")