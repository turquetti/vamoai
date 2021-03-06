#descubra o número que eu estou pensando de (0 a 10):

n = int(input("Digite um número de 0 a 10 e tente adivinhar qual eu estou pensando: "))
while n != 8:
    n = int(input("Hm.. Você ainda não acertou. Digite novamente: "))
print("Acertou! :-)")