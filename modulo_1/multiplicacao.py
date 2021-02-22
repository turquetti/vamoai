from random import randrange

def multiplicacao (n1, n2):
   if (n1 >= 1 and n1 <= 50) and (n2 >= 1 and n2 <= 50):
      return n1*n2

numero1 = randrange(1,50)
numero2 = randrange(1,50)
resultado = multiplicacao(numero1, numero2)

print(f"Os números sorteados foram {numero1} e o {numero2}, o resultado da multiplicação é de {resultado}!")

