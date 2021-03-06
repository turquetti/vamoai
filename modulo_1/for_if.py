maior = 0

for i in range(0,5):
    n = int(input("Digite um número: "))
    if n > maior:
        maior = n

print(f"O maior valor digitado é: {maior}")