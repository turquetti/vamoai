
print('---------------------Questão 1')
class Pessoa:
    def __init__(self, nome, rg):
      self.nome = nome
      self.rg = rg
      self.pai = None
      self.mae = None

print('---------------------Questão 2')
class Pessoa:
  def __init__(self, nome, rg):
    self.nome = nome
    self.rg = rg
    self.pai = None
    self.mae = None
  
  def adiciona_pai(self, pai):
    self.pai = pai

  def adiciona_mae(self, mae):
    self.mae = mae
print('---------------------Questão 3')
class Pessoa:
  def __init__(self, nome, rg):
    self.nome = nome
    self.rg = rg
    self.pai = None
    self.mae = None
  
  def adiciona_pai(self, pai):
    self.pai = pai

  def adiciona_mae(self, mae):
    self.mae = mae

  def eh_mesma_pessoa(self, pessoa):
    self.pessoa = pessoa

    if (self.nome == self.pessoa.nome) and (self.rg == self.pessoa.rg) and (self.mae == self.pessoa.mae):
      
      return True
    else:
      return False

  def eh_antecessor_direto(self, Pessoa):  
    if (self.pai == Pessoa) or (self.mae == Pessoa):
      return True
    else:
      return False
  
  def eh_irmao(self, pessoa):
    self.pessoa = pessoa
    if (self.pai == self.pessoa.pai) and (self.mae == self.pessoa.mae):
      return True
    else:
      return False

print('---------------------Questão 4')
class Pessoa:
  def __init__(self, nome, rg):
    self.nome = nome
    self.rg = rg
    self.pai = None
    self.mae = None
  
  def adiciona_pai(self, pai):
    self.pai = pai

  def adiciona_mae(self, mae):
    self.mae = mae

  def eh_mesma_pessoa(self, pessoa):
    self.pessoa = pessoa

    if (self.nome == self.pessoa.nome) and (self.rg == self.pessoa.rg) and (self.mae == self.pessoa.mae):
      
      return True
    else:
      return False

  def eh_antecessor_direto(self, Pessoa):  
      if (self.pai == Pessoa) or (self.mae == Pessoa):
        return True
      else:
        return False
  
  def eh_irmao(self, pessoa):
    self.pessoa = pessoa
    if (self.pai == self.pessoa.pai) and (self.mae == self.pessoa.mae):
      return True
    else:
      return False
    
def encontre_os_irmaos(lista_pessoas):
  lista_irmaos = []
  lista = []
  
  for i in lista_pessoas:
    for j in lista_pessoas:
      if i.eh_irmao(j):
        lista_irmaos.append(i.nome)
        
  if lista_irmaos == []:
    return lista_irmaos
  else: 
    for irmao in lista_irmaos:
      if irmao not in lista:
        lista.append(irmao)
    return lista

print('---------------------Questão 5')
def balanceado(texto):
  parentesis_1 = texto.count('(')
  parentesis_2 = texto.count(')')
  if texto == []:
    return True
  
  elif (parentesis_1 + parentesis_2) == 0:
    return True
  
  elif (parentesis_1 + parentesis_2) == 1:
    return False
  
  else:
    if parentesis_1 == parentesis_2 and texto[0] in "(":
      return True
    else:
      return False