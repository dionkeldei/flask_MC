from sqlalchemy import Column, Integer, String
from database.db_conn import db
from database.serialize import Serializer

class User(db.Model, Serializer):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String(30))
    password = Column(String(60))

    def serialize(self):
        d = Serializer.serialize(self)
        del d['password']
        return d

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r}, password={self.password!r})"

