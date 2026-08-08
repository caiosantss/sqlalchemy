import os

from sqlalchemy import (
    create_engine, Table, MetaData, select, insert
)

engine = create_engine(str(os.getenv('DB_PATH')), echo=True)

metadata = MetaData()

table = Table(
    'users_test',
    metadata,
    autoload_with=engine # Reflection
)

#DQL
#Query builder
sql = (
        select(table.columns.id, table.columns.name)
       .where(table.columns.name == 'Ambriosio')
)

#DML
sql_insert = (
        insert(table)
        .values(name='Ambriosio')
)

with engine.connect() as conn:
    with conn.begin():
        conn.execute(sql_insert)
        result = conn.execute(sql)
        print(result.fetchall())
