preco_tomate_1a = float(input("Qual foi o preço do quilo do tomate há 1 ano atrás? "))
preco_tomate_hoje = float(input("Qual foi o preço do quilo do tomate hoje? "))
diferenca = preco_tomate_hoje - preco_tomate_1a
inflacao = (diferenca/preco_tomate_1a) * 100
print(f"A diferença de preço do tomate em um ano é de: R$ {diferenca:.1f} reais.")
print(f"A inflação do quilo do tomate em um ano é de: R$ {inflacao:.1f}%.")