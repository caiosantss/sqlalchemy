import os

from sqlalchemy import Column, Integer, String, create_engine, delete, select
from sqlalchemy.orm import DeclarativeBase, Session


engine = create_engine(str(os.getenv('DB_PATH')), echo=True)


class Base(DeclarativeBase):
    ...

class User(Base):
    __tablename__ = 'users_test'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f'Name: {self.name}'

Base.metadata.create_all(engine)

with Session(engine) as s:
    result = s.scalar(
        select(User)
        .where(User.id == 1)
    )

    print(result)

