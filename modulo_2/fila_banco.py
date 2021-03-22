#First In, First Out
class Fila:
    def __init__ (self):
        self.queue = []
    
    def chegada(self, nome):
        self.queue.append(nome)

    def partida(self):
        if self.queue == []:
            return None
        else:
            return self.queue.pop(0)

    def tamanho(self):
        return len(self.queue)

fila_banco = Fila()

print(fila_banco.queue)

fila_banco.chegada("Maria")
fila_banco.chegada("Rita")
fila_banco.chegada("Osvaldo")

print(fila_banco.queue)

print(fila_banco.tamanho())

fila_banco.partida()

print(fila_banco.tamanho())

print(fila_banco.queue)

