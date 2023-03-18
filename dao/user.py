from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_u):
        user = User(**user_u)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_u):
        user = self.get_one(user_u.get("id"))
        user.username = user_u.get("username")
        user.password = user_u.get("password")
        user.role = user_u.get("role")

        self.session.add(user)
        self.session.commit()
