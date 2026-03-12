#entrada
salario = float(input("Digite o salário bruto do funcionário: "))

#processamento
IR = salario * 0.15
INSS = salario * 0.11
SINDICATO = salario * 0.03

LIQUIDO = salario - (IR + INSS + SINDICATO)

#saida
print("O valor do IR é:", IR)
print("O valor do INSS é:", INSS)
print("O valor do sindicato é:", SINDICATO)
print("O salário líquido do funcionário é:", LIQUIDO)

