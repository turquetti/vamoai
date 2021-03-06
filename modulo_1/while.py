n1 = int(input("Digite um número aleatório: "))
n2 = int(input("Digite outro número aleatório: "))

def divisao(n1, n2):
    return n1/n2

while n1 % n2 != 0:
    print("Tente novamente")
    n1 = int(input("Digite um número aleatório: "))
    n2 = int(input("Digite outro número aleatório: "))
    divisao(n1,n2)

print("Divisão sem resto, parabéns!")