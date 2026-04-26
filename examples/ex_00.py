from sqlalchemy import create_engine

engine = create_engine( #Factory : uma fábrica de engines
    'sqlite:///database.db'
)

print(engine)
#Engine(sqlite://)

print(engine.dialect)
#Engine vai ter o dialeto específico do BD que vc esta trabalhando
#<sqlalchemy.dialects.sqlite.pysqlite.SQLiteDialect_pysqlite object at 0x000002FE6669D280>