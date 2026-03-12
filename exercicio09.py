#entrada 
idade = int(input("Digite a sua idade em dias: "))

#processamento
anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30

#saida
print("Você tem", anos, "anos,", meses, "meses e", dias, "dias.")

