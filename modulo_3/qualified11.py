#Questao 1 ---------------------------------------------------------
class Pessoa:
  def __init__(self, nome="João", sobrenome="da Silva", idade=0, genero="Não informado"):
    self.nome = nome
    self.sobrenome = sobrenome
    self.idade = idade
    self.genero = genero
    
  def nomeCompleto(self):
    return f"{self.nome} {self.sobrenome}"

#Questao 2 ---------------------------------------------------------
import random

class Fantasma():
    def __init__(self, cor='branco'):
      self.cor = random.choice(['branco', 'amarelo', 'roxo', 'vermelho'])
    
    def random(self):
      return self.cor

#Questao 3 ---------------------------------------------------------
class Dicionario():
    def __init__(self):
        self.nova_entrada = {}

    def nova_entrada(self, palavra, frase):
        self.nova_entrada[palavra] = frase

    def checar(self,palavra):
        if palavra == self.nova_entrada.keys():
            return self.nova_entrada.values()
        else:
            return f'Não foi possível encontrar a palavra {palavra}'

d = Dicionario()

d.nova_entrada('Maça', 'Uma fruta que cresce em árvores')

#Questao 4 ---------------
class Dicionario():
    def __init__(self):
        self.dic = {}

    def nova_entrada(self, palavra, frase):
        self.dic[palavra] = frase
        return self.dic

    def checar(self, palavra):
        if palavra in self.dic.keys():
            value = self.dic[palavra]
            return value
        else:
            return f'Não foi possível encontrar a palavra {palavra}'