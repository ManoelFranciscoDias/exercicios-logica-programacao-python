# entrada
distancia = float(input("Digite a distância da casa de Maria até a sua irmã: "))
consumo = float(input("Digite o consumo do carro em km/l: "))
preco = float(input("Digite o preço do litro da gasolina: "))

# processamento
litros_necessarios = distancia / consumo
custo_total = litros_necessarios * preco

# saída
print("O custo total da viagem é:", custo_total)
print("A quantidade de litros necessária para a viagem é:", litros_necessarios)

