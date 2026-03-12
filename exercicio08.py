#entrada
fabrica = float(input("Digite o custo da fábrica: "))


#processamento
porcentagem = 1 + (0.28 + 0.45)
custo_final = fabrica * porcentagem

#saida
print("O custo final do carro é:", custo_final)
