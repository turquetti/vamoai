# Questao 6
class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer(), primary_key= True)
    nome = Column(String(255))
    email = Column(String(255))
    data_cadastro = Column(String(255))

class Venda(Base):
    __tablename__ = 'venda'
    id = Column(Integer(), primary_key= True)
    cliente_id = Column(Integer())
    data_venda = Column(String(255))
    f_key = relationship("cliente", back_populates="id")

class Produto_venda(Base):
    __tablename__ = 'produto_venda'
    id = Column(Integer(), primary_key= True)
    venda_id = Column(Integer())
    produto_id = Column(Integer())
    quantidade = Column(Integer())
    f_key_1 = relationship("venda", back_populates="id")
    f_key_2 = relationship("produto", back_populates="id")

# Questao 7
cliente_1 = Cliente(nome='Gabriela') session.add(cliente_1)

#Questao 8
cliente = session.query(Cliente)

#Questao 9
cliente = session.query(Cliente).filter(Cliente.data_cadastro > '2020-01-01')

#Qeustao 10
session.query(Produto).filter(Produto.id == 3).update({'preco': 29.90})

#Questao 11
session.query(Produto).filter(Produto.id == 2).delete()


#Questao 12
c = session.query(Cliente)
session.query(c.id, c.nome, c.sobrenome).filter((Cliente.email.like('%@gmail%')) & (Cliente.data_cadastro > '2019-01-01')

#Questao 13
c = aliased(Cliente)
v = aliased(Venda)
session.query(c.id, c.nome, c.sobrenome,v.id ).join(v.id).filter(v.data_venda > '2020-05-01')

#Questao 14
pv = aliased(Produto_venda))
p = aliased(Produto)
session.query(p.id, sum(pv.quantidade)).join(pv.id).groupby(p.id)
