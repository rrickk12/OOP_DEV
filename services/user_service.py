from models.user import User
from OOP_DEV.app import db
from OOP_DEV.models.user import User

class UserService:

    def get_all_users(self):
        return db_session.query(User).all()

    def get_user_by_id(self, user_id):
        return db_session.query(User).filter(User.id == user_id).first()

    def create_user(self, user_data):
        new_user = User(
            name=user_data['name'],
            age=user_data['age'],
            email=user_data['email'],
            username=user_data['username'],
            password=user_data['password']  # In real-world apps, ensure this is hashed
        )
        db_session.add(new_user)
        db_session.commit()
        return new_user

    def update_user(self, user_id, user_data):
        user = self.get_user_by_id(user_id)
        if user:
            user.name = user_data.get('name', user.name)
            user.age = user_data.get('age', user.age)
            user.email = user_data.get('email', user.email)
            user.username = user_data.get('username', user.username)
            user.password = user_data.get('password', user.password)  # Remember to hash passwords
            db_session.commit()
            return user
        else:
            return None

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            db_session.delete(user)
            db_session.commit()
