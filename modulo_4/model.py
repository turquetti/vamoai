import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Date
from sqlalchemy import inspect

engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/postgres',
    execution_options = {
        "isolation_level": "REPEATABLE READ"
    }
)

metadata = MetaData()

music = Table(
    'music', 
    metadata,
    Column('id', Integer, primary_key=True),
    Column('nome_musica', String),
    Column('artista', String),
)

artist = Table(
    'artist', 
    metadata,
    Column('nome', Integer, primary_key=True),
    Column('n_albums', Integer)
)

metadata.create_all(engine)

inspector = inspect(engine)

print(inspector.get_columns('music'))
print(inspector.get_columns('artist'))
