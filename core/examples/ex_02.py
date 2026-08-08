import os

from sqlalchemy import create_engine

engine = create_engine(
    str(os.getenv('DB_PATH')),
    echo=True
    )

conn_01 = engine.connect()
conn_02 = engine.connect()

conn_01.close()
print(engine.pool.status())
# Pool size: 5  Connections in pool: 1 Current Overflow: -3 Current Checked out connections: 1

conn_03 = engine.connect()
print(engine.pool.status())

'''
- Pool size: 5  Connections in pool: 0 Current Overflow: -3 Current Checked out connections: 2
- Foi usada a conexão que estava na pool, referente a 'conn_01.close()'
'''

'''
- Uma conexão nova do zero pode custar "caro" para a performance da aplicação dependendo do BD.
- Quando fechamos uma conexão, ela é fechada mas fica na lista de pool, quando criamos outra conexões o sqlAlchemy pega a conexão da pool e não cria uma nova literalmente.
- Essa fila de pool é para ser reciclada automaticamente das mais antigas para as mais novas, o objetivo é deixar a aplicação mais performática.

'''