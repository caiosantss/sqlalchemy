import os

from sqlalchemy import create_engine

engine = create_engine(
    str(os.getenv('DB_PATH')), 
    echo=True
    )

conn = engine.connect()
#Return a new _engine.Connection object: type: Connection
#conn: sqlalchemy.engine.base.Connection

print(conn.connection.dbapi_connection)
'''
sqlite3.Connection object at x
Usa o próprio conector do driver que estamos usando - regra da DBApi
'''
conn.close()