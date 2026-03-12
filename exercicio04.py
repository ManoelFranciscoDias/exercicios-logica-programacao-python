import math

#entrada
raio = float(input("Digite o raio da lata de oleo: "))
altura = float(input("Digite a altura da lata de oleo: "))

#processamento
volume = (math.pi) * (raio ** 2) * (altura)

#saida
print("O volume da lata de oleo é:", volume)