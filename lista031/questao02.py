'''
Elaborar um programa que pergunte quatro valores inteiros e apresente 2 resultados:
a) Resultado de suas adições
b) Resultado de suas multiplicações
'''

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
num3 = int(input("Informe outro número: "))
num4 = int(input("Informe um último número: "))


soma = num1 + num2 + num3 + num4
mult = num1 * num2 * num3 * num4

print(f"A soma destes números é {soma}.")
print(f"E a multiplicação destes números é {mult}.")