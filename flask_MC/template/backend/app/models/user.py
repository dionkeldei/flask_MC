from sqlalchemy import Column, Integer, String, TEXT
from database.db_conn import db
from database.serialize import Serializer

class User(db.Model, Serializer):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String(30))
    password = Column(TEXT)

    def serialize(self):
        d = Serializer.serialize(self)
        del d['password']
        return d
    
    def serializeComplete(self): # To retrieve password ( FOR LOGIN )
        d = Serializer.serialize(self)
        return d

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r}, password={self.password!r})"

def allUsers():
    users = User.query.all()
    return User.serialize_list(users)

def findUser(id):
    user = User.query.get(id)
    return user.serialize()

def findUserWhere(params):
    filters = []
    for key, value in params.items():
        if hasattr(User, key):
            filters.append(getattr(User, key) == value)

    users = User.query.filter(*filters).all()
    return User.serialize_list(users)

def setUser(params):
    new_user = User(**params)
    db.session.add(new_user)
    db.session.commit()
    return True