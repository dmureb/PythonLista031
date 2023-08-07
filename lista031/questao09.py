'''
Fazer um algoritmo que pergunte 1 número e apresente:
a) O próprio número
b) O quadrado deste número
c) A raiz quadrada deste número
'''
import math

num = float(input("Informe um número: "))
print("O número escolhido foi: ", num)
print("O quadrado deste número é: ", math.pow(num,2))
print("A raiz quadrada deste número é: ", math.sqrt(num))