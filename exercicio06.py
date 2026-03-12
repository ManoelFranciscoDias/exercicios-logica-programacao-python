import math

# entrada
x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))

x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))

# processamento
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# saída
print("A distância entre os pontos é:", d)