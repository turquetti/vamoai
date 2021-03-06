#Vamos contar até 10 pulando de 2 em 2!
n = int(input("Digite o início da contagem: "))
p = int(input("Digite o passo da contagem: "))
f = int(input("Digite o final da contagem: "))

for i in range(n,f,p):
    print(f"{i}")
