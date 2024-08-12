import time

#2) Faça um programa em que o usuário precisa cadastrar nome, idade, telefone e e-mail. Depois mostre os valores digitados na tela.
nomeCliente = input("Qual seu nome? ")
print(f"Seja bem-vindo/a, {nomeCliente}")

time.sleep(3)
print(f"Vamos precisar cadastrar umas informações, tudo bem?")
time.sleep(2)

idadeCliente = float(input("Qual é a sua idade?: "))
print(f"Legal..")
time.sleep(2)

telefoneCliente = float(input("Qual seu número? Insira no seguinte formato: (+5511123456789)"))
print(f"Certo..")
time.sleep(2)

emailCliente = input("Seu e-mail?")
time.sleep(2)

print(f"Certo..")
time.sleep(3)

print(f"Para conferir, vou listar todas as informações que você cadastrou")
time.sleep(2)

print() 
print() 
print() 
print() 
print(f"*******************************")
print(f"Nome: {nomeCliente}: ")
print(f"Idade: {idadeCliente}: ")
print(f"Telefone: {telefoneCliente}: ")
print(f"E-mail: {emailCliente}: ")
print(f"*******************************")


