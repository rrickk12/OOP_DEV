from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'personas'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def get_full_details(self):
        return f'Name: {self.name}, Age: {self.age}, Email: {self.email}'

    def update_details(self, name=None, age=None, email=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if email:
            self.email = email
