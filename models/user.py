from sqlalchemy import Column, String
from models.persona import Persona

class User(Persona):
    __tablename__ = 'users'

    username = Column(String)
    password = Column(String)

    def __init__(self, name, age, email, username, password):
        super().__init__(name, age, email)
        self.username = username
        self.password = password

    def get_user_details(self):
        persona_details = super().get_full_details()
        return f'{persona_details}, Username: {self.username}'

    def update_username(self, new_username):
        self.username = new_username
