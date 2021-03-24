# Restaurantes -----------------------------------------------------------
class Restaurante():
    def __init__(self, cardapio, dias_aberto):
        self.cardapio = cardapio
        self.dias_aberto = dias_aberto
    
    def informacoes_restaurante(self):
        print("="*100)
        print(f"""
        Nome do Restaurante: {self.nome}
        Cardapio: {self.cardapio}
        Dias de funcionamento: {self.dias_aberto}
        Formas de Pagamento: {self.pagamento}
        """)
        print("="*100)

    def mensagem(self):
        print("Pedido Recebido")

class Outback(Restaurante):
    def __init__(self, nome, pagamento, cardapio, dias_aberto):
        super().__init__(cardapio, dias_aberto)
        self.nome = nome
        self.pagamento = pagamento

class BurguerKing(Restaurante):
    def __init__(self, nome, pagamento, cardapio, dias_aberto):
        super().__init__(cardapio, dias_aberto)
        self.nome = nome
        self.pagamento = pagamento

class Jeronimo(Restaurante):
    def __init__(self, nome, pagamento, cardapio, dias_aberto):
        super().__init__(cardapio, dias_aberto)
        self.nome = nome
        self.pagamento = pagamento

#Pessoa -----------------------------------------------------------
class Pessoa():
    def __init__(self, nome, cpf, telefone, rg):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.rg = rg
    
    def informacoes_pessoa(self):
        print("="*100)
        print(f"""
        Nome: {self.nome}
        CPF: {self.cpf}
        RG: {self.rg}
        Telefone: {self.telefone}
        """)
        print("="*100)
        
class PessoaEntregadora(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, distancia):
        super().__init__(nome, cpf, telefone, rg)
        self.distancia = distancia

    def mensagem(self):
        print("Pedido a ser entregue.")

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, cupom20off):
        super().__init__(nome, cpf, telefone, rg)
        self.cupom20off = cupom20off 
        
    def mensagem(self):
        print("Pedido Entregue")

class ProprietariaRestaurante(Pessoa):
    def __init__(self, nome, cpf, telefone, rg):
        super().__init__(nome, cpf, telefone, rg)
    
    def mensagem(self):
        print("Pedido à Confirmar")

