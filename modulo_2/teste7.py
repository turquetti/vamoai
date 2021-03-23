# #Questao 1
# def cria_pilha():
#     pilha = []
#     return pilha

# def tamanho(pilha):
#     tamanho = len(pilha)
#     return tamanho

# def adiciona(pilha, elemento):
#     pilha.append(elemento)
#     return pilha

# def remove(pilha):
#   if pilha == []:
#     return None
#   else:
#     item = pilha[-1]
#     pilha.pop(-1)
#     return item


# #Questao 2
# # Preencha as funções
# def cria_fila():
#     fila = []
#     return fila

# def tamanho(fila):
#     tamanho = len(fila)
#     return tamanho

# def adiciona(fila, valor):
#     fila.append(valor)
#     return fila

# def remove(fila):
#     if fila == []:
#       return None
#     else:
#       item = fila[0]
#       fila.pop(0)
#       return item

#Questao 3

#Questao4
# Preencha as funções
def cria_pilha():
    pilha = []
    return pilha

def tamanho(pilha):
    tamanho = len(pilha)
    return tamanho

def adiciona(pilha, elemento):
    pilha.append(elemento)
    return pilha

def remove(pilha):
  if pilha == []:
    return None
  else:
    item = pilha.pop(-1)
    return item

# print(remove(['a', 'b', 'c']))

def inverte_texto(texto):
    itens = ""
    item = ""
    pilha = cria_pilha()
    if texto == "":
      return ""
    else:
      for i in range(0, len(texto)):
          adiciona(pilha, texto[i])

    for i in range(0, len(pilha)):
        item += remove(pilha)
    return item

print(inverte_texto('abcd'))