def somarimposto(valor,taxa):
    precofinal = valor + (valor *(taxa/100))
    return precofinal
 
valor = float(input("digite o valor do produto: "))
taxa = float(input("digite o valor do imposto: "))
print(somarimposto(valor,taxa))
