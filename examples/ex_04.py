import os

from sqlalchemy import create_engine, text, inspect, Table, MetaData

engine = create_engine(str(os.getenv('DB_PATH')), echo=True)
inspected = inspect(engine)
metadata = MetaData()

table = Table(
    'users_test',
    metadata,
    autoload_with=engine # Reflection: _schema.Table object will be reflected
)

#Refatorar
with engine.connect() as conn:
    with conn.begin():
        query_create = text('CREATE TABLE IF NOT EXISTS users_test (id INTEGER PRIMARY KEY, name TEXT UNIQUE)')
        conn.execute(query_create)

    with conn.begin():
        query_insert = text('INSERT INTO users_test (name) VALUES (:name) ON CONFLICT (name) DO NOTHING')
        conn.execute(query_insert, {'name': 'Alice'})

    with conn.begin():
        query_select = text('SELECT * FROM users_test')
        result = conn.execute(query_select)
        print(result.fetchall())