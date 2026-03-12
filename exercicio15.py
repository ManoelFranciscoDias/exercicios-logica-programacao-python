# entrada
modelo = input("Digite o modelo do carro: ")
marca = input("Digite a marca do carro: ")
ano = int(input("Digite o ano do carro: "))
km_inicial = float(input("Digite a quilometragem inicial: "))
km_final = float(input("Digite a quilometragem final: "))
litros_consumidos = float(input("Digite os litros de combustível consumidos: "))
preco_por_litro = float(input("Digite o preço por litro de combustível: "))

# processamento
distancia_percorrida = km_final - km_inicial
total_a_pagar = litros_consumidos * preco_por_litro
km_por_litro = distancia_percorrida / litros_consumidos

# saida
print(f"Modelo_______________________ {modelo}")
print(f"Marca________________________ {marca}")
print(f"Ano__________________________ {ano}")
print(f"Distância percorrida__________ {distancia_percorrida:.2f} km")
print(f"Litros de combustível consumidos {litros_consumidos:.2f} L")
print(f"Preço por litro R$ ___________ {preco_por_litro:.2f}")
print(f"Total a pagar R$ ____________ {total_a_pagar:.2f}")
print(f"Km por litro _________________ {km_por_litro:.2f}")