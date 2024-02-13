from werkzeug.security import generate_password_hash
from app.extensions import db

import enum

class Role(enum.Enum):
    ADMIN = 1
    MANAGER = 2
    USER = 3

class Manager(db.Model):
    manager_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(100))
    password = db.Column(db.String(255))  # Storing hashed password
    role  = db.Column(db.Enum(Role), default=Role.MANAGER)

    def __repr__(self):
        return f'<Manager "{self.user_name}">'

    @property
    def _password(self):
        return self._password

    @_password.setter
    def _password(self, _password):
        # Hash the password before storing it
        self.password = generate_password_hash(_password)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(user_name=username).one()


# Register event listener to hash password before insertion
@db.event.listens_for(Manager, "before_insert")
def hash_password_before_insert(mapper, connection, target):
    if target.password:
        target.password = generate_password_hash(target.password)


# Register event listener to hash password before update
@db.event.listens_for(Manager, "before_update")
def hash_password_before_update(mapper, connection, target):
    if target.password:
        target.password = generate_password_hash(target.password)
