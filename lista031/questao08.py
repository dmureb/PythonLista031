'''
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro.
'''

dist = float(input("Qual a distância percorrida na viagem? "))
cmedio = float(input("Qual é o valor do consumo médio do automóvel, em quilômetros por litro? "))
litros = dist / cmedio
print("A distância percorrida na viagem é de ", dist, "quilômetros e o valor do consumo médio do automóvel é de ", cmedio, "quilômetros por litro." )
print("A quantidade de litros que o automóvel gastará em sua viagem é: ", litros, "litros." )