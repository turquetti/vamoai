nome1 = input("Digite o nome do primeiro produto: ")
preco1 = float(input("Digite o preço do primeiro produto: "))

nome2 = input("Digite o nome do segundo produto: ")
preco2 = float(input("Digite o preço do segundo produto: "))

nome3 = input("Digite o nome do terceiro produto: ")
preco3 = float(input("Digite o preço do terceiro produto: "))

print('-'*30)
print('CARRINHO DE COMPRAS')
print('-'*30)
print(f'''
[ 1 ] {nome1} no valor de R$ {preco1} reais.
[ 2 ] {nome2} no valor de R$ {preco2} reais.
[ 3 ] {nome3} no valor de R$ {preco3} reais.
''')
print('-'*30)

if preco1 < preco2 and preco1 < preco3:
    menor = preco1
    print(f"O produto mais barato é o {nome1} no valor de R$ {preco1} reais.")
elif preco2 < preco1 and preco2 < preco3:
    menor = preco2
    print(f"O produto mais barato é o {nome2} no valor de R$ {preco2} reais.")
else:
    menor = preco3 
    print(f"O produto mais barato é o {nome3} no valor de R$ {preco3} reais.")
