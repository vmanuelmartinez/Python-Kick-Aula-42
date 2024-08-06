n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

media = (n1+n2+n3) / 3 

if(media < 6):
    print(f"*************************************")
    print(f"Reprovado, a media foi {media:.2f}")
elif(media >= 6):
    print(f"*************************************")
    print("Aprovado, sua media foi de {media:.2f}!")



