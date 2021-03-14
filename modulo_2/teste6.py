#qualified - Semana 6

#questão 1
def adiciona_chave_e_valor():
    dicionario = {"1+1": 2, "1+2": 3}
    dicionario['1+3'] = 4
    return dicionario

#questão 2
def lista_para_dicionario(lista):
    dic = {}
    if lista == []:
      dic = {}
      return dic
    else:
      for i in lista:
        dic[i] = i
      return dic

#questao 3
def soma_valores(dicionario):
    if dicionario == {}:
      return 0
    
    else:
        soma = 0
        for i in dicionario:
            soma += dicionario[i]
        
        return soma

print(soma_valores({"a": 1, "b": 2, "c": 2}))

#questao4
def verifica_chave (dicionario,chave):

    if dicionario == {}:
        return False

    for i in dicionario:
        chaves = dicionario.keys()

        if (chave in chaves):
            return True
        else:
            return False


print(verifica_chave({"a": 1, "b": 2, "c": 2}, "a"))
print(verifica_chave({}, "a"))

# Questao 5
def listas_para_dicionario(lista1, lista2):
  if (lista1 == [] and lista2 == []) or (len(lista1) != len(lista2)):
    dic = {}
    return dic
  else:
    dic = {}
    dic = dict(zip(lista1,lista2))

print(listas_para_dicionario(["a", "b", "c"], [1, 2, 3]))

#ou sem zip:

def listas_para_dicionario(lista1, lista2):
  if (lista1 == [] and lista2 == []) or (len(lista1) != len(lista2)):
    dic = {}
    return dic
  else:
    dic = {}
    
    for i in range(0,len(lista1)):
      dic[lista1[i]] = lista2[i]
    return dic

print(listas_para_dicionario(["a", "b", "c"], [1, 2, 3]))

#Questao 6

def conta_letras(string):
    if string == "":
      dic = {}
      return dic
    
    else:
        dic = {}
        c = 0

        for i in string:
            c = dic.get(i,0)
            c += 1
            dic[i] = c

        return dic

print(conta_letras("aAAbBbbb"))