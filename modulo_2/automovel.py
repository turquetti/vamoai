class Automovel:
    def __init__(self, tipo, modelo, ano, quilometragem):
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem
    
    def info_automovel(self):
        print(f"""
        Tipo: {self.tipo}
        Modelo: {self.modelo}
        Ano: {self.ano}
        Quilometragem rodada (km): {self.quilometragem} 
        """)
    

class Carro(Automovel):
    pass

carro = Carro("Carro", "Up!", "2015", "110.000")
carro.info_automovel()


class Moto(Automovel):
    pass

moto = Moto("Moto", "Honda", "2010", "50.100")
moto.info_automovel()

