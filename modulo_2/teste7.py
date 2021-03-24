# #Questao 1
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


#Questao 2
def cria_fila():
    fila = []
    return fila

def tamanho(fila):
    tamanho = len(fila)
    return tamanho

def adiciona(fila, valor):
    fila.append(valor)
    return fila

def remove(fila):
    if fila == []:
      return None
    else:
      item = fila.pop(0)
      return item

#Questao 3
def insere_par_remove_impar(lista):
    pilha = cria_pilha()
    if tamanho(lista) == []:
      return 0
    elif lista == []:
      return []
    
    else:
        for i in lista:
            if i % 2 == 0:
                adiciona(pilha, i)
            else:
                remove(pilha)
        return pilha
    
print(insere_par_remove_impar([1, 2, 1, 2, 1]))
print(insere_par_remove_impar([1, 2, 3, 4, 5, 6, 7, 8]))

#Questao4
Preencha as funções
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

# #Questao 5
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

def palindromo(s):
    item = ""
    pilha = cria_pilha()

    for i in range(0, len(s)):
        adiciona(pilha, s[i])

    for i in range(0, len(pilha)):
        item += remove(pilha)

    if s == item:
        return True
    else:
        return False
print(palindromo('batata'))


# #Questão 6
def cria_fila():
    fila = []
    return fila

def tamanho(fila):
    tamanho = len(fila)
    return tamanho

def adiciona(fila, valor):
    fila.append(valor)
    return fila

def remove(fila):
    if fila == []:
      return None
    else:
      item = fila.pop(0)
      return item

def cria_fila():
    fila = []
    return fila

def tamanho(fila):
    tamanho = len(fila)
    return tamanho

def adiciona(fila, valor):
    fila.append(valor)
    return fila

def remove(fila):
    if fila == []:
      return None
    else:
      item = fila.pop(0)
      return item

# # Esse codigo passou sem o remove!
def fila_prioridade(lista):
    fila_preferencial = cria_fila()
    fila_normal = cria_fila()
    
    if tamanho(lista) == []:
      return 0
    elif lista == []:
      return []
    else: 
      for i in lista:
          if i >= 65:
              adiciona(fila_preferencial, i)
          else:
              adiciona(fila_normal, i)
      fila = fila_preferencial + fila_normal
      return fila

# #Usando o remove!
def fila_prioridade(lista):
    fila_preferencial = cria_fila()
    fila_normal = cria_fila()
    
    if tamanho(lista) == []:
      return 0
    elif lista == []:
      return []
    else: 
      while len(lista) > 0:
          if lista[0] >= 65:
            item = remove(lista)
            adiciona(fila_preferencial, item)
          else:
            item = remove(lista)
            adiciona(fila_normal, item)
            
      fila = fila_preferencial + fila_normal
      return fila

#Questao 7
def balanceado(texto):
  parentesis_1 = texto.count('(')
  parentesis_2 = texto.count(')')
  if parentesis_1 == parentesis_2:
    return True
  else:
    return False
