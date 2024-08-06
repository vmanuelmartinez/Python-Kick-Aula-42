#cadastrar nome, preço, quantidade, código , total a se pagar


nomedoproduto = input("Insira o nome do produto: ")
preco = float(input("Qual o preço do produto? "))  
quantidade = int(input("Quantidade do produto: "))  
codigo = input("Código do Produto: ")  
Avalor_total = preco * quantidade 

print(f"O nome do produto é {nomedoproduto}, o preço foi de {preco}, a quantidade é {quantidade}, com o código {codigo} e o valor total foi de {valor_total}")

