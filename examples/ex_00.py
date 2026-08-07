import os

from sqlalchemy import create_engine

engine = create_engine( #Factory : uma fábrica de engines
    str(os.getenv('DB_PATH'))
)

print(engine)
#Engine(sqlite://)

print(engine.dialect)
#Engine vai ter o dialeto específico do BD que vc esta trabalhando
#<sqlalchemy.dialects.sqlite.pysqlite.SQLiteDialect_pysqlite object at 0x000002FE6669D280>