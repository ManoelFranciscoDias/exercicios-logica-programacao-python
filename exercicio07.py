# entrada
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
d = float(input("Digite d: "))
e = float(input("Digite e: "))
f = float(input("Digite f: "))

# Calcular denominador
den = (a*e - b*d)

# Calcular x e y
x = (c*e - b*f) / den
y = (a*f - c*d) / den

# saida
print("Valor de x:", x)
print("Valor de y:", y)

