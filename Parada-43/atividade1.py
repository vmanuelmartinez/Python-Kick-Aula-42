peso = float(input("Por favor, digite seu peso: "))
altura = float(input("Qual sua altura?: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Magreza!")
elif 18.5 <= imc <= 24.9:
    print("Normal")
elif 25.0 <= imc < 29.9:
    print("Sobrepeso!")
elif 30.0 <= imc < 39.9:
    print("Obesidade!")
else:
    print("Obesidade grave!!")