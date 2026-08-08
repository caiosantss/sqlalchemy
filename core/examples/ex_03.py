import os

from sqlalchemy import create_engine, text

engine = create_engine(str(os.getenv('DB_PATH')), echo=True)

with engine.connect() as conn:
    with conn.begin():
        query_create = text('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT UNIQUE)')
        conn.execute(query_create)

    with conn.begin():
        query_insert = text('INSERT INTO users (name) VALUES (:name)')
        conn.execute(query_insert, {'name': 'Alice'})

    with conn.begin():
        query_select = text('SELECT * FROM users')
        result = conn.execute(query_select)
        print(result.fetchall())