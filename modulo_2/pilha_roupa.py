class Pilha():
    def __init__(self):
        self.stack = []
    
    def adiciona_roupa(self, roupa):
        self.stack.append(roupa)
    
    def dobra_roupa(self):
        if self.tamanho == 0:
            return None
        else:
            self.stack.pop()
    
    def tamanho(self):
        return len(self.stack)

pilha_roupa = Pilha()

print(pilha_roupa.stack)

pilha_roupa.adiciona_roupa("Camiseta Vermelha")
pilha_roupa.adiciona_roupa("Calça Jeans")
pilha_roupa.adiciona_roupa("Meia")

print(pilha_roupa.stack)

pilha_roupa.dobra_roupa()

print(pilha_roupa.stack)
