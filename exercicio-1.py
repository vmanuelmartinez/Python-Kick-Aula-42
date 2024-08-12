#Faça um programa em que o usuário digita dois valores e o resultado da soma é exibido na tela.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = num1 + num2

print(f"**************************************")
print(f"A soma dos dois valores é: {resultado:.0f}") #:.2f limitamos as casas decimais em Python.
print(f"**************************************")