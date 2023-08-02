'''
Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
valor +	(valor x (taxa : 100) x	tempo em dias).
'''

valor = float(input("Qual é o valor da prestação atrasada? "))
taxa = float(input("Qual é o valor da taxa? "))
dias = float(input("Qual é o tempo do atraso, em dias? "))
print("O valor final da prestação em atraso é de R$", valor + (valor * (taxa / 100) * dias))