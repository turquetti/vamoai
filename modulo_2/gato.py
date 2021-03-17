class Gato:
    def __init__(self, nome, cores, qtd_cores, raca):
        self.nome = nome
        self.cores = cores
        self.qtd_cores = qtd_cores
        self.raca = raca

    def comer(self, racao, quantidade):
           self.racao = racao
           self.quantidade = quantidade
    
    def dormir(self, lugar):
        self.lugar = lugar

    def miar(self):
        print("Meow!")
