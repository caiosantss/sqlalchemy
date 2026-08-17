import os

from sqlalchemy import Column, Integer, String, create_engine, delete, select, Engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


engine: Engine = create_engine(str(os.getenv('DB_PATH')), echo=True)
#Factory of session
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    ...

class User(Base):
    __tablename__ = 'users_test'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f'Name: {self.name}'

Base.metadata.create_all(engine)

with Session() as s:
    result = s.scalar(
        select(User)
        .where(User.id == 1)
    )

    print(result)

