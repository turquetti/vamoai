#Questao 1)
def summation(num):
    sum = 0
    list = []
    if num >= 0:
      for i in range(0,num+1):
          list.append(i)

      for i in range(1,len(list)):
          sum += list[i]
    
    return sum

#Questao2)
def array_plus_array(arr1,arr2):
    arr3 = arr1 + arr2
    sum = 0
    for i in range(0,len(arr3)):
        sum += arr3[i]
    
    return sum

#Questao3)
def create_phone_number(lista):
    return (f"({lista[0]}{lista[1]}{lista[2]}) {lista[3]}{lista[4]}{lista[5]}-{lista[6]}{lista[7]}{lista[8]}{lista[9]}")
    
#Questao4)
def reverse_string(str):
    frase = ""

    for i in range(0, len(str)):
        frase += str[i]
    
    frase = frase[::-1]

    return frase


#Questao 5)
def positive_sum(arr):
    sum = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
           sum += arr[i]
        if arr == []:
            return 0

    return sum

#Questão 6)
def find_smallest(numbers):
    menor = numbers[0]

    for i in numbers:
        if i < menor:
            menor = i
    return menor

print(find_smallest([1,2,3,4,5,6,7,8,9,10]))
print(find_smallest([1,2,3,4,5,6,7,8,-9,10]))

#Questão 7)

def distinct(seq):
    lista = []

    for i in seq:
        if i not in lista:
            lista.append(i)

    return lista

print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))

#Questão 8)

def complete_series(seq):
   testar_lista = []
   for i in seq:
       if i not in testar_lista:
           testar_lista.append(i)
       else:
           testar_lista = [0]
           return testar_lista
    
    lista2 = []
    maximo = max(seq)
    for i in range(0, (maximo+1)):
        lista2.append(i)
    return lista2


print(complete_series([3,4,4,5]))


fila_prioridade = [18, 23, 65, 89]
fila_normal = []
for i in fila_prioridade:
    if i <= 65:
        item = remove(fila_prioridade)
        adiciona(fila_normal, item)
print(fila_prioridade, fila_normal)