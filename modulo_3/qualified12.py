#Questao 1 --------------------------------------------------------------------
# def filtroAmigo(x):
#   lista_amigos = []
#   for i in x:
#     if len(i) == 4:
#       lista_amigos.append(i)
#   return lista_amigos

#Questao 2 --------------------------------------------------------------------

# def array_diff(a,b):
#     lista = []
#     if a == []:
#         return []
#     elif b == []:
#         return a
#     else:
#         for i in a:
#           if i not in b:
#             lista.append(i)
#         return lista

#Questao 3 --------------------------------------------------------------------
# def count_sheeps(sheep):
#     c = 0
#     for i in sheep:
#         if i == True:
#             c += 1
#     print(c)

# count_sheeps([True,  True,  True,  False, True,  True,  True,  True , True,  False, True,  False, True,  False, False, True , True,  True,  True,  True , False, False, True,  True ])

#Questao 4 --------------------------------------------------------------------
# def find_all(array, n):
#     lista = []

#     if n not in array:
#         return []
#     else:
#         c = 0
#         for i in array:
#             if n == i:
#                 lista.append(c)
#             c += 1
#         print(lista)
            
# find_all([10, 1, 20, 16, 14, 11, 20, 2, 17, 16, 14], 16)

#Questao 5 --------------------------------------------------------------------

def conta_letras(string):
    dic = {}
    c = 1
    if string == "":
        return {}
    else:
        for i in string:
            dic[i] = dic.get(i, 0) + 1
        print(dic)


conta_letras("abc")
conta_letras("AAAAA")
conta_letras("AaaBBb")
conta_letras("")